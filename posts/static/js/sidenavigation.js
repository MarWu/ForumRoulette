function openNav() {
    document.getElementById("sideNavigation").style.width = "200px";
    document.getElementById("content").style.marginLeft = "200px";
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

function likeComment() {
    document.getElementById("like_comment").style.color="green";
}

function dislikeComment() {
    document.getElementById("dislike_comment").style.color="red";
}