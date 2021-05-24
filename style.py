stylesheet = """
  MainWindow {
    font-family: Inter;
    min-width: 800px;
    min-height: 453px;
    max-height: 453px;
  }
  
  QFrame#background {
    min-width: 784px;
    min-height: 440px;
    max-width: 784px;
    max-height: 440px;
    background: white;
    background-image: url(\"static/Bg_figures.svg\");
    background-attachment: local;
    background-repeat: no-repeat;
    padding: 8px;
  }
  
  QLabel#login-title {
    color: #000000;
    width: 215px;
    height: 24px;
    font-size: 16px;
    font-weight: bold;
    line-height: 24px;
    margin: 24px 0px;
  }
  
  QLineEdit#input-form {
    max-width: 280px;
    max-height: 32px;
    padding-left: 16px;
    padding-right: 16px;
    padding-top: 6px;
    padding-bottom: 6px;
    background-color: #ffffff;
    border-radius: 15px;
    border: 1px solid #C1C7CD;
  }
  
  QCheckBox#keep-cbox {
    margin-top: 18px;
  }

  QPushButton#login-button {
    max-width: 311px;
    max-height: 32px;
    background: #4D4DD1;
    color: white;
    margin-left: 1px;
    padding-top: 8px;
    padding-bottom: 8px;
    border-radius: 16px;
  }
  
  QPushButton#forgot-button {
    color: #343A3F;
    margin: 10px 0px;
    border: none;
  }

  QLineEdit#code-otp-item {
    border: 1px solid black;
    padding: 12px;
    max-width: 16px;
    max-height: 32px;
    font-size: 14px;
    text-align: center;
    margin-left: 6px;
  }
  
  QLabel#enter-confirmation-label {
    height: 40px;
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
    text-align: center;    
    color: #121619;
    margin: 16px 0px;
  }
  
  QLabel#expire-timer-title {
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;
    margin: 16px 0px;
    color: #000000;
  }
  
  QLabel#expire-timer-value {
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;
    margin: 16px 0px;
    color: #064ada;
  }
  
  QPushButton#resend-password-button {
    padding: 6px 16px;
    
    min-width: 280px;
    min-height: 32px;
    max-width: 280px;
    max-height: 32px;
        
    border: 1px solid #343A3F;
    border-radius: 20px;
    margin: 24px 0px;
  }
  
  QFrame#framed-component {
    background-color: #F2F4F8; 
    border-radius: 8px;
  }
  
  #connect-status-component QFrame {
    min-width: 768px;
    max-width: 768px;
    max-height: 48px;
    min-height: 48px;
  }
  
  #token-status-component {
    min-width: 376px;
    max-width: 376px; 
    min-height: 376px;
    max-height: 376px;
    
    
  }
  
  QLabel#connect-status-label {
    max-width: 556px;
    min-width: 556px;
    max-height: 16px;
    min-height: 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;
    letter-spacing: -0.08px;
    color: #121619;
    padding: 0;
    margin-top: 12px;
  }
  
  QLabel#status-icon {
    margin-top: 8px;
    max-width: 28px;
    min-width: 28px;
    min-height: 28px;
    background-image: url(\"static/Exclamation.svg\");
    background-repeat: no-repeat;
  }
  
  #round-input-hover-icon {
    max-width: 48px;
    min-width: 48px;
    max-height: 48px;
    min-height: 48px;
    background-image: url(\"static/Input_hover.png\");
    background-repeat: no-repeat;
    background-position: left center;
    background-origin: content;
  }
  
  
  #round-input-icon {
    max-width: 48px;
    min-width: 48px;
    max-height: 48px;
    min-height: 48px;
    background-image: url(\"static/Input.png\");
    background-repeat: no-repeat;
    background-position: left center;
    background-origin: content;
  }
  
  #otp-round-input {
    max-width: 30px;
    min-width: 30px;
    max-height: 30px;
    min-height: 30px;
    background-color: #ffffff;
    border: none;
  }
  
  QPushButton#connect-btn {
    background-color: #4D4DD1; 
    border-radius: 8px; 
    max-width: 144px;
    min-width: 144px; 
    max-height: 32px;
    min-height: 32px;
    margin-bottom: 8px;
    margin-right: 8px;
    height: 20px;
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
    text-align: center;

    color: #FFFFFF;
  }
  
  QLabel#item-title {
    margin-left: 13px;
    min-width: 344px;
    min-height: 12px;
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0.12px;
    color: #A2A9B0;
  }
  
  QLabel#item-title-with-top-margin {
    margin-top: 13px;
    margin-left: 13px;
    min-width: 344px;
    min-height: 12px;
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0.12px;
    color: #A2A9B0;
  }
  
  QLabel#item-value {
    margin-left: 9px;
    margin-top: 0px;
    min-width: 344px;
    min-height: 32px;    
    font-style: normal;
    font-weight: bold;
    
    font-size: 24px;
    line-height: 32px;
    color: #000000;
    padding-bottom: 12px;
  }
  
  QLabel#item-value-usd {
      margin-top: 0px;
      margin-bottom: 0px;
      margin-left: 10px;
      min-width: 74px;
      max-height: 24px;
      font-style: normal;
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      color: #000000;
      padding-bottom: 0;
  }
  
  QLabel#item-pseudo-border {
    min-width: 380px;
    min-height: 1px;
    max-height: 1px;
    background: #DDE1E6;
    margin: 0px;
  }
  
  QLabel#cp-item-pseudo-border {
    min-width: 410px;
    max-width: 410px;
    min-height: 1px;
    max-height: 1px;
    background: #DDE1E6;
    margin-top: 16px;
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 16px;
  }
  
  QLabel#item-percent-value {
    margin-top: 3px;
    margin-bottom: 0;
    width: 45px;
    height: 16px;
    left: 82px;
    top: 4px;
    font-style: normal;
    font-weight: bold;
    font-size: 12px;
    line-height: 16px;    
    color: #1FCB30;
  }
  
  #network-stats-component {
    min-width: 407px;
    max-width: 407px;
    min-height: 170px;
  }
  
  QLabel#speed-title {
    width: 344px;
    height: 12px;
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0.12px;
    color: #A2A9B0;
    margin-top: 13px;
    margin-left: 13px;
  }
  
  QLabel#download-title {
    width: 218px;
    max-height: 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;    
    color: #4D5358;
    margin-left: 11px;
    margin-bottom: 0px;
    padding-bottom: 0px;
  }
  
  QLabel#download-value {
    width: 218px;
    height: 32px;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 32px;    
    color: #000000;
    margin-left: 9px;
    margin-top: 0px;
  }
  
  #storage-stats-component {
    min-width: 407px;
    max-width: 407px;
    max-height: 175px;
    min-height: 175px;
  }
  
  #margin-helper-capasity-slider {
    max-width: 235px;
    padding-left: 18px;
  }
  
  QLabel#storage-title {
    width: 344px;
    height: 12px;
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0.12px;    
    color: #A2A9B0;
    
    margin-top: 13px;
    margin-left: 13px;
  }
  
  QLabel#active-used-icon {
    margin-top: 5px;
    min-width: 48px;
    min-height: 48px;
    background-image: url(\"static/product.png\");
    background-repeat: no-repeat;
    margin-left: 13px;
  }
  
  QLabel#available-storage-icon {
    margin-top: 5px;
    min-width: 48px;
    min-height: 48px;
    background-image: url(\"static/kuncun.png\");
    background-repeat: no-repeat;
    margin-left: 13px;
  }
  
  QLabel#active-used-title {
    max-width: 288px;
    min-height: 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;    
    color: #4D5358;
    margin-top: 3px;
    margin-bottom: 0;
    margin-left: 2px;
  }
  
  QLabel#active-used-value {
    max-width: 288px;
    min-height: 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;    
    color: #000000;
    margin-top: 0;
    margin-left: 0.5px;
  }
  
  FramedComponent QFrame {
    margin: 8px;
  }
  
  #background-popup {
    min-width: 400px;
    min-height: 400px;
    max-width: 400px;
    max-height: 400px;
    background: #FFFFFF;
    
    border: 1px solid #E6E6E6;
    border-radius: 7px;
  }
  
  #connect-dialog {
    background-color: transparent;
  }
  
  QLabel#connect-popup-label {
    width: 336px;
    height: 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.08px;
    color: #000000;
    margin-left: 16px;
    margin-top: 16px;
  }
  
  #foreground-popup {
    min-width: 800px;
    min-height: 453px;
    background: rgba(0, 0, 0, 0.5);
  }
  
  QLabel#connect-popup-close-button {
      margin-top: 24px;
      margin-left: 216px;
      background-image: url(\"static/close.png\");
      background-attachment: local;
      background-repeat: no-repeat;
  }
  
  QLabel#cp-info-message-label {    
    margin-top: 12px;
    margin-bottom: 12px;
    margin-left: 20px;
    color: white;
    background: #6767E6;
    padding-top: 12px;
    padding-bottom: 12px;
    padding-left: 16px;
    padding-right: 16px;
    border-radius: 8px;
  }
  
  QLabel#set-capacity-title {
    width: 368px;
    height: 16px;    
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;    
    color: #000000;
    margin-top: 16px;
    margin-left: 16px;
    margin-bottom: 22px;
  }
  
  #select-capacity-component {
    margin-left: 16px;
  }
  
  QSlider#capacity-slider {
    max-width: 232px;
  }
  
  QLabel#capacity-value {
    max-width: 120px;
    min-height: 32px;    
    border: 1px solid #DDE1E6;
    border-radius: 16px;
    margin: 0px 16px;
    padding-left: 9px;
  }
  
  QLabel#set-lease-time-title {
    max-width: 368px;
    max-height: 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 16px;    
    color: #000000;
    margin: 16px 0px;
    margin-left: 16px;
  }
  
  QComboBox#lease-value-box {
    max-width: 200px;
    max-height: 32px;
    
    padding-left: 6px;
    margin-left: 22px;
    border: 1px solid #DDE1E6;
  }
  
  QLabel#cp-cancel-button {
    min-width: 79px;
    min-height: 32px;
    border: 1px solid #343A3F;
    border-radius: 16px;
    margin-right: 9px;
  }
  
  QLabel#cp-start-button {
    min-width: 66px;
    min-height: 32px;
    background: #4D4DD1;
    color: white;
    border-radius: 16px;
    margin-right: 16px;
  }
  
  #day-picker-body {
    padding: 1px;
    min-width: 83px;
    min-height: 22px;
    max-width: 83px;
    max-height: 22px;
    background: #ebecee;
    
    border-radius: 5px;
  }
  
  QLabel#picker-button {
    margin-top: 1px;
    margin-left: 1px;
    min-width: 25px;
    min-height: 20px;
    max-width: 25px;
    max-height: 20px;
    border-radius: 5px;
  }
  
  QLabel#picker-button-active {
    background: #FFFFFF;
    margin-top: 1px;
    margin-left: 1px;
    min-width: 25px;
    min-height: 20px;
    max-width: 25px;
    max-height: 20px;
    border-radius: 5px;
  }
  
  #connect-popup-footer {
    min-height: 80px;
    margin-top: 0px;
  }
  
  #combo-box {
    min-width: 200px;
    min-height: 32px;
    max-width: 200px;
    max-height: 32px;
    border: 1px solid #DDE1E6;
    border-radius: 14px;
    margin-left: 18px;
    margin-bottom: 0px;
    padding-left: 16px;
  }
  
  #combo-box-container {
    min-width: 240px;
    min-height: 200px;
    background: red;
    border: 1px solid #E6E6E6;
    border-radius: 7px;
  }
  
  #combo-box-value {
    min-width: 170px;
  }
  
  #combo-box-open-button {
    min-width: 16px;
    min-height: 16px;
    background-image: url(\"static/vector.png\");
    background-attachment: local;
    background-repeat: no-repeat;
    margin-top: 14px;
    margin-left: 11px;
  }
  
  #ok-message-title {
    min-width: 368px;
    min-height: 48px;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    
    text-align: center;    
    color: #000000;
    margin-top: 0px;
  }
  
  #ok-message-image {
    min-width: 368px;
    min-height: 360px;
    background-image: url(\"static/User_profile_intro.png\");
    background-attachment: local;
    background-repeat: no-repeat;
    margin-bottom: 0px;
    padding-bottom: 0px;
  }
  
  #lease-controller-body {
    min-width: 752px;
    max-width: 752px;
    max-height: 48px;
    min-height: 48px;
    background-color: #F2F4F8; 
    border-radius: 8px;
    margin-left: 8px;
    margin-top: 8px;
    margin-bottom: 5px;
    padding-left: 16px;
  }
  
  #lease-time-message {
    min-width: 178px;
    min-height: 24px;
    background: #C9DEFF;
    border-radius: 8px;
    font-style: normal;
    font-weight: normal;
    font-size: 10px;
    line-height: 16px;    
    color: #054ADA;
    margin: 0px 10px;
    padding-left: 8px;
  }
  
  #stop-lease-button {
    min-width: 24px;
    min-height: 24px;
    background-image: url(\"static/Stop.png\");
    background-attachment: local;
    background-repeat: no-repeat;
    margin-left: 88px;
  }
  
  #pause-lease-button {
    min-width: 24px; min-height: 24px;
    background-image: url(\"static/Pause.png\");
    background-attachment: local;
    background-repeat: no-repeat;
    margin-left: 16px;
  }
  
  #release-button {
    min-width: 178px;
    min-height: 32px;
    max-width: 178px;
    max-height: 32px; 
    background: #054ADA;
    border-radius: 8px;
    margin-left: 16px;
  }
  
  #release-button-title {
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
    color: #FFFFFF;
    padding-left: 16px;
  }
"""