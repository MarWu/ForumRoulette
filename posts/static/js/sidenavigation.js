function openNav() {
    document.getElementById("sideNavigation").style.width = "200px";
    document.getElementById("content").style.marginLeft = "200px";
}

function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("content").style.marginLeft = "0";
}

function likepost() {
    document.getElementById(`like`).style.color="green";
}

function dislikepost() {
    document.getElementById(`dislike`).style.color="red";
}

function like(count) {
    document.getElementById(`like_${count}`).style.color="green";
}

function dislike(count) {
    document.getElementById(`dislike_${count}`).style.color="red";
}

function likeComment(count) {
    document.getElementById(`like_comment_${count}`).style.color="green";
}

function dislikeComment(count) {
    document.getElementById(`dislike_comment_${count}`).style.color="red";
}