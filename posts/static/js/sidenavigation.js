function openNav() {
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("content").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("content").style.marginLeft = "0";
}

function like() {
    document.getElementById("like").style.color="green";
}

function dislike() {
    document.getElementById("dislike").style.color="red";
}