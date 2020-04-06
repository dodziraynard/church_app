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

const alertBox = document.querySelector(".alert-box");
if (alertBox){
    alertBox.addEventListener("click", ()=>{
        alertBox.style.display="none";
    })
}

const updateRequestViewStatus = (target)=>{
    const pk = target.dataset.pk
    target.innerText = "..."
    const csrfmiddlewaretoken    = document.querySelector("input[name='csrfmiddlewaretoken']").value
    const url = `/view_request/${pk}`
    $.post( url, 
        {
            csrfmiddlewaretoken
        }, 
    function(data){
        response = data.success
        if (response===true){
            target.classList.remove("btn-info")
            target.classList.add("btn-success")
            target.innerText = "OK"
            target.disabled=true;
        }
    });
}