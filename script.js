const form = document.getElementById('form');
const input = document.getElementById('input');
const timeInput = document.getElementById('time');
const todosUL = document.getElementById('todos');

// Load todos from local storage
const todos = JSON.parse(localStorage.getItem('todos')) || [];

// Display existing todos from local storage
todos.forEach(todo => addTodoUI(todo));

// Event listener for form submission
form.addEventListener('submit', function(e) {
  e.preventDefault();
  addTodo();
});

// Function to add a new todo
function addTodo() {
  const todoText = input.value.trim();
  const todoTime = timeInput.value.trim();

  if (todoText && todoTime) {
    const todo = {
      text: todoText,
      time: todoTime,
      completed: false
    };

    todos.push(todo);
    addTodoUI(todo);
    updateLocalStorage();
    input.value = '';
    timeInput.value = '';
  }
}

// Function to add todo UI
function addTodoUI(todo) {
  const todoEl = document.createElement('li');
  todoEl.classList.add('todo-item');

  const completeCircle = document.createElement('span');
  completeCircle.classList.add('complete-circle');
  if (todo.completed) {
    completeCircle.classList.add('completed');
    todoEl.classList.add('completed');
  }

  const textSpan = document.createElement('span');
  textSpan.innerText = `${todo.text} - ${todo.time}`;

  const deleteButton = document.createElement('button');
  deleteButton.innerText = '✖';
  deleteButton.classList.add('delete-button');

  // Toggle completed status on circle click
  completeCircle.addEventListener('click', function() {
    todo.completed = !todo.completed;
    todoEl.classList.toggle('completed');
    completeCircle.classList.toggle('completed');
    updateLocalStorage();
  });

  // Remove todo on delete button click
  deleteButton.addEventListener('click', function() {
    const index = todos.indexOf(todo);
    if (index !== -1) {
      todos.splice(index, 1);
      todoEl.remove();
      updateLocalStorage();
    }
  });

  todoEl.appendChild(completeCircle);
  todoEl.appendChild(textSpan);
  todoEl.appendChild(deleteButton);

  todosUL.appendChild(todoEl);
}

// Function to update local storage
function updateLocalStorage() {
  localStorage.setItem('todos', JSON.stringify(todos));
}
