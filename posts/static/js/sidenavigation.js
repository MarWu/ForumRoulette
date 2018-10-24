function openNav() {
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

function like() {
    document.getElementById("like").style.color="green";
}

function dislike() {
    document.getElementById("dislike").style.color="red";
}