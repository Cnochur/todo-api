export default function TodoList({ tasks, STATUS_OPTIONS, editTask, deleteTask, updateStatus }) {
  
  const GROUPED_TASKS = {
    NEW: tasks.filter(task => task.status === "NEW"),
    IN_PROGRESS: tasks.filter(task => task.status === "IN_PROGRESS"),
    COMPLETE: tasks.filter(task => task.status === "COMPLETE"),
  };

  return (
    <div className="row g-3">

      {Object.entries(GROUPED_TASKS).map(([status, columnTasks]) => (
        <div key={status} className="col-12 col-md-4">

          <div className="card h-100 shadow-sm">
            <div className="card-body">

              <h5 className="card-title mb-3">
                {STATUS_OPTIONS[status]}
              </h5>

              {columnTasks.map(task => (
                <div key={task.id} className="card mb-2">

                  <div className="card-body p-2">

                    <div className="d-flex justify-content-between align-items-start">
                      <strong>{task.title}</strong>

                      <div className="btn-group btn-group-sm gap-2">
                        <button
                          className="btn btn-outline-primary"
                          onClick={() => editTask(task)}
                        >
                          ✏️
                        </button>

                        <button
                          className="btn btn-outline-danger"
                          onClick={() => deleteTask(task.id)}
                        >
                          ❌
                        </button>
                      </div>
                    </div>

                    <p className="text-muted small mb-2">
                      {task.description}
                    </p>

                    <select
                      className="form-select form-select-sm"
                      value={task.status}
                      onChange={(e) => updateStatus(task.id, e.target.value)}
                    >
                      {Object.entries(STATUS_OPTIONS).map(([key, label]) => (
                        <option key={key} value={key}>
                          {label}
                        </option>
                      ))}
                    </select>

                  </div>
                </div>
              ))}

            </div>
          </div>

        </div>
      ))}

    </div>
  );
}