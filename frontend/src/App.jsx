import { useEffect, useState } from "react";
import axios from "axios";
import TodoList from "./components/KanBan";

const API_URL = "http://127.0.0.1:8000/tasks/";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const tempUserID = 1;
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [editingTaskID, setEditingTaskID] = useState(null);

  const STATUS_OPTIONS = {
    NEW: "New",
    IN_PROGRESS: "In Progress",
    COMPLETE: "Complete",
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const result = await axios.get(API_URL);
    setTasks(result.data);
  };

  const addTask = async () => {
    if (!title.trim()) return;

    if (editingTaskID) {
      await axios.put(`${API_URL}edit/${editingTaskID}/`, {
        title,
        description,
      });
      setEditingTaskID(null);
    } else {
      await axios.post(`${API_URL}add/`, {
        user_id: tempUserID,
        title,
        description,
      });
    }

    setTitle("");
    setDescription("");
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await axios.delete(`${API_URL}delete/${id}/`);
    fetchTasks();
  };

  const editTask = (task) => {
    setEditingTaskID(task.id);
    setTitle(task.title);
    setDescription(task.description);
  };

  const updateStatus = async (id, newStatus) => {
    await axios.patch(`${API_URL}update/${id}/`, {
      status: newStatus,
    });
    fetchTasks();
  };

  return (
    <div className="container py-4">

      {/* HEADER FORM */}
      <div className="card shadow-sm mb-4">
        <div className="card-body">

          <h4 className="mb-3">
            {editingTaskID ? `Editing: ${title || "Untitled task"}` : "Add Task"}
          </h4>

          <div className="mb-2">
            <label htmlFor="taskTitle">Title</label>
            <input
              className="form-control mb-2"
              id="taskTitle"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Task title..."
            />
            <label htmlFor="taskDescription">Descrtiption</label>
            <input
              className="form-control"
              id="taskDescription"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="What does it involve?"
            />
          </div>

          <div className="d-flex gap-2">
            <button
              className={`btn ${editingTaskID ? "btn-warning" : "btn-primary"}`}
              onClick={addTask}
            >
              {editingTaskID ? "Update" : "Add"}
            </button>

            {editingTaskID && (
              <button
                className="btn btn-outline-secondary"
                onClick={() => {
                  setEditingTaskID(null);
                  setTitle("");
                  setDescription("");
                }}
              >
                Cancel
              </button>
            )}
          </div>

        </div>
      </div>

      {/* KANBAN BOARD */}
      <TodoList
        tasks={tasks}
        STATUS_OPTIONS={STATUS_OPTIONS}
        editTask={editTask}
        deleteTask={deleteTask}
        updateStatus={updateStatus}
      />
    </div>
  );
}