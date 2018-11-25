function openNav() {
    if (document.documentElement.clientWidth < 750) {
            document.getElementById("sideNavigation").style.width = "200px";
            document.getElementById("content").style.display = "none";
    }
    else {
        document.getElementById("sideNavigation").style.width = "200px";
        document.getElementById("content").style.marginLeft = "200px";
    }

}

function closeNav() {
        if (document.documentElement.clientWidth < 750) {
            document.getElementById("sideNavigation").style.width = "0px";
            document.getElementById("content").style.display = "flex";
    }
    else {
        document.getElementById("sideNavigation").style.width = "0px";
        document.getElementById("content").style.marginLeft = "0px";
    }
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("content").style.marginLeft = "0";
}

