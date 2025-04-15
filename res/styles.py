# styles.py
def custom_css():
    return """
        <style>
        [data-testid="stDecoration"] {
            background: #FFFFFF00;
        }
        .dash-title {
            font-size: 45px;
            font-weight: bold;
            background: -webkit-linear-gradient(270deg, #184700FF, #CD9A00FF);
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
            color: #B6A573FF;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .colored-subtitle {
            font-size: 30px;
            font-weight: bold;
            color: #433D29FF;
            display: inline-block;
            padding: 5px 5px;
            text-decoration: none;``
        }

        .colored-text {
            font-size: 20px;
            font-weight: bold;
            color: #8F7E48FF;
            display: inline-block;
            padding: 5px 5px;
            border-radius: 10px;
            text-decoration: none;``
        }

        div.stRadio > label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }

        .stButton > button {
            color: white;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            padding: none;
            border: none;
            width: 100px;
            transition: 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            text-align: center;
            align-items: center;
            background: linear-gradient(to bottom, #B38600FF, #594300FF);
            transform: scale(1.05);
        }
    </style>

    
    """
