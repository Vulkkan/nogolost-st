# styles.py
def custom_css():
    return """
        <style>
        [data-testid="stDecoration"] {
            background: #FFFFFF00;
        }
        .dash-title {
            font-size: 70px;
            font-weight: bold;
            background: -webkit-linear-gradient(270deg, #184700FF, #37A600FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .title {
            font-size: 50px;
            font-weight: bold;
            background:  #184700FF;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .centered-title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(270deg, #184700FF, #49DB00FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            font-size: 30px;
            background: -webkit-linear-gradient(270deg, #000000FF, #000000FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .centered-subtitle {
            font-size: 30px;
            text-align: center;
            color: #D6FFC2FF;
            background: #244B11FF;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .colored-subtitle {
            font-size: 30px;
            font-weight: bold;
            color: #FFFFFFFF;
            display: inline-block;
            padding: 5px 5px;
            background-color: #6EA138FF;
            border-radius: 10px;
            text-decoration: none;``
        }

        .centered-text {
            font-size: 18px;
            text-align: center;
            font-weight: normal;
            background: #113200FF;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .colored-text {
            font-size: 20px;
            font-weight: bold;
            color: #205F00FF;
            display: inline-block;
            padding: 5px 5px;
            color: #D6FFC2FF;

            border-radius: 10px;
            text-decoration: none;``
        }
        .wrapped-text {
            font-size: 16px;
            font-weight: normal;
            color: black;
            display: inline-block;
        }

        div.stRadio > label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }

        .stButton > button {
            color: white;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            padding: none;
            border: none;
            width: 150px;
            transition: 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            text-align: center;
            align-items: center;
            background: linear-gradient(to bottom, #46D300FF, #319200FF);
            transform: scale(1.05);
        }
    </style>

    
    """
