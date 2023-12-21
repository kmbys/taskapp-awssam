function show_tasks() {
    const xhr = new XMLHttpRequest();
    xhr.addEventListener('load', function() {
        console.log(this.responseText);
        document.getElementById("tasks").textContent = this.responseText;
    })
    xhr.open('GET', '/Prod/tasks');
    xhr.send();
}

function add_task() {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/Prod/tasks');
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
        document.getElementById('new_task').value = '';
        show_tasks();
    }
    xhr.send(JSON.stringify({'title': document.getElementById('new_task').value}));
}
