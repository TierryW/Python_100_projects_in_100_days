import streamlit as st
import streamlit.components.v1 as components # Inserir página html no streamlit

st.set_page_config(page_title="Calculator",page_icon="🧮",layout="centered")

st.title("🧮 Calculator")

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Calculator</title>
</head>

<body>

<div class="calculator">

    <input
        type="text"
        id="display"
        readonly
        placeholder="0">

    <div class="buttons">

        <button class="function" onclick="clearDisplay()">C</button>
        <button class="function" onclick="backspace()">⌫</button>
        <button class="operator" onclick="append('/')">/</button>
        <button class="operator" onclick="append('*')">*</button>

        <button onclick="append('7')">7</button>
        <button onclick="append('8')">8</button>
        <button onclick="append('9')">9</button>
        <button class="operator" onclick="append('-')">-</button>

        <button onclick="append('4')">4</button>
        <button onclick="append('5')">5</button>
        <button onclick="append('6')">6</button>
        <button class="operator" onclick="append('+')">+</button>

        <button onclick="append('1')">1</button>
        <button onclick="append('2')">2</button>
        <button onclick="append('3')">3</button>
        <button class="equal" onclick="calculate()">=</button>

        <button class="zero" onclick="append('0')">0</button>
        <button onclick="append('.')">.</button>

    </div>

    <div class="history">

        <h3>History</h3>

        <div id="history-list"></div>

    </div>

</div>
<style>

body{
    margin:0;
    background:#0f172a;
    font-family:Arial, Helvetica, sans-serif;
}

.calculator{

    width:360px;
    margin:30px auto;
    background:#1e293b;
    border-radius:20px;
    padding:20px;
    box-shadow:0 15px 40px rgba(0,0,0,.45);

}

#display{

    width:100%;
    height:70px;
    box-sizing:border-box;
    border:none;
    outline:none;
    border-radius:15px;
    background:#111827;
    color:white;
    font-size:34px;
    text-align:right;
    padding:15px;
    margin-bottom:15px;

}

.buttons{

    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:10px;

}

button{

    height:65px;
    border:none;
    border-radius:15px;
    font-size:24px;
    cursor:pointer;
    transition:.2s;
    background:#334155;
    color:white;

}

button:hover{

    transform:scale(1.05);
    filter:brightness(115%);

}

button:active{

    transform:scale(.95);

}

.operator{

    background:#FFA07A;

}

.operator:hover{

    background:#E9967A;

}

.function{

    background:#475569;

}

.equal{

    background:#22c55e;
    grid-row:span 2;

}

.equal:hover{

    background:#4ade80;

}

.zero{

    grid-column:span 2;

}

.history{

    margin-top:20px;
    background:#111827;
    border-radius:15px;
    padding:15px;
    max-height:180px;
    overflow-y:auto;

}

.history h3{

    margin-top:0;
    color:white;

}

.history-item{

    color:#cbd5e1;
    border-bottom:1px solid #334155;
    padding:6px 0;

}

</style>
<script>

const display = document.getElementById("display");

const history = document.getElementById("history-list");

function append(value){

    display.value += value;

}

function clearDisplay(){

    display.value = "";

}

function backspace(){

    display.value = display.value.slice(0,-1);

}

function calculate(){

    try{

        const expression = display.value;
        let result = eval(expression);
        result = Number(result.toFixed(2));
        addHistory(expression, result.toFixed(2));
        display.value = result.toFixed(2);

    }

    catch{

        display.value = "Error";

    }

}

function addHistory(expression, result){

    const item = document.createElement("div");
    item.className = "history-item";
    item.innerHTML = `${expression} = ${result}`;
    history.prepend(item);

}

});

</script>
</body>
</html>
"""

components.html(html, height=750, scrolling=False)
