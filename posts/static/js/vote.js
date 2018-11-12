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
