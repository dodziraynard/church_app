// Sidebar
const sideBar = document.querySelector(".sidebar");
hideSidebar = ()=>{
    sideBar.classList.toggle("hide-sidebar");
    sideBarOpened = localStorage.getItem("sideBarOpened");
    if (sideBarOpened === "true"){
        localStorage.setItem("sideBarOpened", false);
    } else{
        localStorage.setItem("sideBarOpened", true);
    }
}
const toggleButton = document.querySelector("#toogleSidebar");
let sideBarOpened = localStorage.getItem("sideBarOpened");
if (sideBarOpened === "true"){
    sideBar.classList.add("hide-sidebar")
} else{
    sideBar.classList.remove("hide-sidebar")
}

if (toggleButton){
    toggleButton.addEventListener("click", hideSidebar);
}

