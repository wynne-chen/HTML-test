import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <head>
	<title> General Assembly - DSI 37 </title>
	<link rel="stylesheet" href="style.css">
	<link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
	<style> 
		body {
			background-color:#fed500;
		}
        img {
            display: vertical-align;
        }
        
        h1 {
            font-size:100px;
            font-family:Roboto;
	    font-weight: 900;
        }
        
        div {
            font-size:50px;
            font-family:"Montserrat";
        }
        
	#languages {
            font-size:80px;
            font-family:"Montserrat";
	    font-weight: bold;
        }
	
        .centre{
            display: block;
	        margin-left: auto;
	        margin-right: auto;
	        width: 50%;
        }
    
        marquee{
            font-size:100px; 
	        font-family:impact;"
        }
    
        .pLink{
            background-color: #FD9AA7;
            border: none;
            color: white;
            padding: 20px 34px;
            text-align: center;
            text-decoration: none;
            font-family:Montserrat;
            display: inline-block;
            font-size: 20px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 15px;
	    box-shadow: 2px 5px #F3F1E5
        }
        
	.pLink:hover{
            background-color: #F94A65;
        }
	
        .pLink:active{
            background-color: #F94A65;
	    box-shadow: 1px 2px #F3F1E5;
	    transform: translateY(3px);
	    transform: translateX(1px);
	    
        }

	</style>

</head>
    
    <h1> Test Portfolio For DSI 37 </h1>
    
    <img src ="https://gamepress.gg/pokemongo/sites/pokemongo/files/2020-06/600px-025Pikachu-Libre.png"
	class="centre"; 
	alt="Pika pika!!"
	/>
    
    <div> I am a junior data scientist specialising in </div>
    <div id="languages">Python and Machine Learning.</div>
    
    <hr />
    
    <button class="pLink" onclick= "window.open('https://github.com/wynne-chen/DSI-37-Project-1.git', '_blank')"> Climate Change and Food Delivery </button>
    <br>
    <button class="pLink" onclick= "window.open('https://github.com/wynne-chen/DSI-37-Project-2.git', '_blank')"> HDB Resale Price Predictor </button>
    
    """,
	width = 660,
    	height = 1480,
)
