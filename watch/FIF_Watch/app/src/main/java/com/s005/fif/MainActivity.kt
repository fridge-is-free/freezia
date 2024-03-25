/* While this template provides a good starting point for using Wear Compose, you can always
 * take a look at https://github.com/android/wear-os-samples/tree/main/ComposeStarter and
 * https://github.com/android/wear-os-samples/tree/main/ComposeAdvanced to find the most up to date
 * changes to the libraries and their usages.
 */

package com.s005.fif

import android.app.AlarmManager
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.provider.Settings
import android.util.DisplayMetrics
import android.util.Log
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.wear.compose.material.MaterialTheme
import androidx.wear.compose.navigation.rememberSwipeDismissableNavController
import androidx.wear.tooling.preview.devices.WearDevices
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.messaging.FirebaseMessaging
import com.s005.fif.fcm.RecipeLiveData
import com.s005.fif.navigation.NavigationDestination
import com.s005.fif.timer.ui.TimerViewModel
import com.s005.fif.ui.theme.FIF_WatchTheme
import com.s005.fif.ui.FIFWatchApp
import com.s005.fif.utils.AlarmUtil.alarmManager
import com.s005.fif.utils.ScreenSize.screenHeightDp
import com.s005.fif.utils.ScreenSize.screenWidthDp
import dagger.hilt.android.AndroidEntryPoint
import javax.inject.Inject

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    private val timerViewModel: TimerViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()

        super.onCreate(savedInstanceState)

        setTheme(android.R.style.Theme_DeviceDefault)

        getScreenSize(resources.displayMetrics)

        getFCMToken()

        setContent {
            val navController = rememberSwipeDismissableNavController()

            FIF_WatchTheme {
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .background(MaterialTheme.colors.background),
                    contentAlignment = Alignment.Center
                ) {
                    FIFWatchApp(navController)
                }
            }

            RecipeLiveData.isRecipeConnected.observe(this) { isRecipeConnected ->
                if (isRecipeConnected) {
                    navController.navigate(NavigationDestination.RecipeDetail.route) {
                        launchSingleTop = true
                    }
                }
            }

            RecipeLiveData.recipeStep.observe(this) { step ->
                if (RecipeLiveData.isRecipeConnected.value!! && step != 0) {
                    navController.navigate("${NavigationDestination.RecipeStep.route}/$step") {
                        launchSingleTop = true
                    }
                }
            }
        }

        alarmManager = this.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val hasPermission = alarmManager!!.canScheduleExactAlarms()

        if (!hasPermission) {
            val intent = Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM)
            startActivity(intent)
        }
    }

    override fun onRestart() {
        super.onRestart()
        val alarmManager = this.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val hasPermission = alarmManager.canScheduleExactAlarms()

        if (!hasPermission) {
            Toast.makeText(this, "FIF를 실행하기 위해서는 알람 권한이 필요합니다", Toast.LENGTH_SHORT).show()
            this.finish()
        }
    }

    // 스크린 사이즈 측정
    private fun getScreenSize(displayMetrics: DisplayMetrics) {
        screenHeightDp = displayMetrics.heightPixels / displayMetrics.density
        screenWidthDp = displayMetrics.widthPixels / displayMetrics.density
    }


    private fun getFCMToken() {
        FirebaseMessaging.getInstance().token.addOnCompleteListener(OnCompleteListener { task ->
            if (!task.isSuccessful) {
                Log.d("로그", "MainActivity - getFCMToken() 호출됨 / 토큰 가져오기 실패")
                return@OnCompleteListener
            }

            val token = task.result

            Log.d("로그", "MainActivity - getFCMToken() 호출됨 / 토큰 가져오기 성공 ${token}")
        })
    }

    override fun onStart() {
        super.onStart()

        timerViewModel.getTimerList()
    }

    override fun onStop() {
        super.onStop()

        timerViewModel.saveTimerListDataStore()
    }


    override fun onDestroy() {
        super.onDestroy()
        Log.d("로그", "MainActivity - onDestroy() 호출됨")
    }
}