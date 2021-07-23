function revertCard(id){
    document.getElementById(id).style.opacity = .85
    document.getElementById(id).style.color = "darkgray"
    return true
}
module.exports = revertCard