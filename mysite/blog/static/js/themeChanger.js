var FONTSIZE = 1;


function changeTheme(fontColor, backgroundColor) {
    document.getElementsByTagName("body")[0].style.backgroundColor = backgroundColor;
    document.getElementsByTagName("body")[0].style.color = fontColor;
    var links = document.getElementsByTagName("a")
    for (let i = 0; i < links.length; i++){
        links[i].style.color = fontColor;
    }
    // var dropDownMenus = document.getElementsByClassName("dropdown-menu");
    // for (let i = 0; i < dropDownMenus.length; i++){
    //     links[i].style.backgroundColor = backgroundColor;
    // }

}

function changeFontSize(parametr) {
    setFONTSIZE(parametr);
    document.getElementsByTagName("article")[0].style.fontSize = `${getFONTSIZE()}em`;
}

function setFONTSIZE(par) {
    FONTSIZE += par;
}

function getFONTSIZE() {
    return copiedFONTSIZE = FONTSIZE;

}

var adjustWindow = {
    lightBut: {},
    darkBut: {},
    sepiaBut: {},
    incFontBut: {},
    decFontBut: {},

    buttonConnect: function (lightButton, darkButton, sepiaButton, incFontButton, decFontButton) {
        this.lightBut = document.getElementById(lightButton);
        this.darkBut = document.getElementById(darkButton);
        this.sepiaBut = document.getElementById(sepiaButton);
        this.incFontBut = document.getElementById(incFontButton);
        this.decFontBut = document.getElementById(decFontButton);

        this.lightBut.onclick = () => changeTheme("#000000", "#ffffff");
        this.darkBut.onclick = () => changeTheme("#9e9893", "#3f3f3f");
        this.sepiaBut.onclick = () => changeTheme("#000000", "#f5af4b");
        this.incFontBut.onclick = () => changeFontSize(+0.2);
        this.decFontBut.onclick = () => changeFontSize(-0.2);

    }
}

adjustWindow.buttonConnect("light", "dark", "sepia", "inc-font", "dec-font");
