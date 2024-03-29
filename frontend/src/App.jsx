import { useState, useEffect } from 'react';
// import startRecognition from './utils/voiceRecognization';
import ScreenFrame from './components/ScreenFrame';

import './assets/styles/main.css';
import { setToken } from './utils/firebase';
import { setWatchToken } from './apis/firebase';
import navigateInstance from './utils/navigate';

function App() {
  const [focused, setFocused] = useState(
    sessionStorage.getItem('focused') &&
      sessionStorage.getItem('focused') !== 'undefined'
      ? JSON.parse(sessionStorage.getItem('focused'))
      : false,
  );
  const [onScreen, setOnScreen] = useState(false);
  const { navigate } = navigateInstance;

  useEffect(() => {
    // startRecognition();
    setToken();
    setWatchToken(import.meta.env.VITE_TMP_WATCH_TOKEN);
  }, []);
  useEffect(() => {
    if (focused) {
      if (
        sessionStorage.getItem('focused') &&
        sessionStorage.getItem('focused') !== 'undefined' &&
        JSON.parse(sessionStorage.getItem('focused')) === focused
      ) {
        setOnScreen(true);
      } else {
        setTimeout(() => {
          setOnScreen(true);
        }, 700);
      }
    } else setOnScreen(false);

    sessionStorage.setItem('focused', JSON.stringify(focused));
  }, [focused]);

  return (
    <div>
      <div className="background-crop">
        <img
          className={`${
            sessionStorage.getItem('focused') &&
            sessionStorage.getItem('focused') !== 'undefined' &&
            JSON.parse(sessionStorage.getItem('focused'))
              ? 'background-in'
              : 'background-out'
          } ${focused ? 'focus-in' : 'focus-out'}`}
          src="/images/background.png"
          alt="background"
          onClick={() => {
            setFocused(!focused);
          }}
        />
      </div>
      {onScreen && <ScreenFrame />}
      {/* <div id="container">
        <div id="result" />
      </div> */}
      {!focused && (
        <div
          className="open-door-button"
          onClick={() => {
            setFocused(true);
            navigate('/Cooking/warning');
          }}
        />
      )}
    </div>
  );
}

export default App;
