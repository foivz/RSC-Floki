/**
 * Created by Davor Obilinovic on 22/05/14.
 */


// Strings manipulation
if (typeof String.prototype.startsWith != 'function') {
    String.prototype.startsWith = function (str){
        return this.indexOf(str) == 0;
    };
}

if (typeof String.prototype.endsWith != 'function') {
    String.prototype.endsWith = function (str){
        return this.indexOf(str) == this.length - str.length;
    };
}

if (typeof String.prototype.contains != 'function') {
    String.prototype.contains = function (str){
        return this.indexOf(str) != -1;
    };
}

if (typeof String.prototype.removeSubstring != 'function') {
    String.prototype.removeSubstring = function (str){
        return this.substr(0,this.indexOf(str))+this.substr(this.indexOf(str)+str.length)
    };
}

function showModal(TITLE,TEXT,BTNL_TEXT,BTNR_TEXT,BTNR_ACTION ){
    options ={
        keyboard:false
    };
    var mod = $('#msModal');
    var content = mod.children().children().children();
    var title = content.children()[1];
    var text = content[1];
    var btnr = content[2].children[1];
    var btnl = content[2].children[0];
    title.innerHTML = TITLE;
    text.innerHTML = TEXT;
    btnl.innerHTML = BTNL_TEXT;
    btnr.innerHTML = BTNR_TEXT;
    btnl.setAttribute("onclick","preventDefault()");
    btnr.setAttribute("onclick",BTNR_ACTION);
    mod.modal(options);
}

function showElement(element){
    return removeClassAttribute(element,"hidden");
}

function hideElement(element){
    return appendClassAttribute(element,"hidden");
}

function appendClassAttribute(element, attribute){
    var classString = element.className;
    if (!(classString.startsWith(attribute+" ") ||
          classString.contains(" "+attribute+" ") ||
          classString.endsWith(" " + attribute) )){
        classString = (classString + " " + attribute).trim();
        element.className = classString;
        return classString
    }
    return classString
}

function removeClassAttribute(element, attribute){
    var classString = element.className;
    if (classString.startsWith(attribute+" " ))
        classString = classString.removeSubstring(attribute+" ");
    if (classString.contains(" "+attribute+" "))
        classString = classString.removeSubstring(" "+attribute);
    if (classString.endsWith(" "+attribute))
        classString = classString.removeSubstring(" "+attribute);
    element.className = classString;
    return classString
}

function flash(message){
    var box = $("#jsMessageBox")[0];
    var content = $("#jsMessageContent")[0];
    content.innerHTML = message;
    showElement(box);
}