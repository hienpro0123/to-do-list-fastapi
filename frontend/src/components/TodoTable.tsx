"use client";

import { useEffect, useState } from "react";
import { Todo } from "../../types";
import Task from "./Task";

export default function TodoTable() {
  const [todo_list, setTodoList] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTodos = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const headers: any = {};
        if (token) headers["Authorization"] = `Bearer ${token}`;

        const response = await fetch("http://localhost:8000/todos/", {
          cache: "no-store",
          headers,
        });

        if (response.ok) {
          const data = await response.json();
          const sorted_todos: Todo[] = data.sort((a: Todo, b: Todo) => a.id - b.id);
          setTodoList(sorted_todos);
        }
      } catch (err) {
        console.error("Failed to fetch todos:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchTodos();
  }, []);

  if (loading) {
    return <div className="p-4 text-center">Loading tasks...</div>;
  }

  return (
    <table className="w-full">
      <thead className="w-full">
        <tr className="w-full flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md">
          <th>Task</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        {todo_list.map((task: Todo) => (
          <Task key={task.id} task={task} />
        ))}
      </tbody>
    </table>
  );
}
