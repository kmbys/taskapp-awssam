function show_tasks() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/Prod/tasks');
    xhr.responseType = 'text';
    xhr.onload = () => {
        document.getElementById("tasks").value = this.response;
    }
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
