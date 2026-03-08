"use client";

import { useEffect, useState } from "react";
import { Todo } from "../../types";
import Task from "./Task";

export default function TodoTable() {
  const [todo_list, setTodoList] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState<"all" | "completed" | "pending">("all");

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

        // Build query parameters
        const params = new URLSearchParams();
        if (search) {
          params.append("search", search);
        }
        if (statusFilter !== "all") {
          params.append("status", statusFilter);
        }

        const url = `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/todos/?${params.toString()}`;

        const response = await fetch(url, {
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
  }, [search, statusFilter]);

  if (loading) {
    return <div className="p-4 text-center">Loading tasks...</div>;
  }

  return (
    <div>
      {/* Search and Filter Section */}
      <div className="mb-4 flex gap-4 flex-wrap items-center">
        {/* Search Input */}
        <input
          type="text"
          placeholder="Search tasks..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="flex-1 min-w-[200px] px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-600"
        />

        {/* Status Filter Dropdown */}
        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value as "all" | "completed" | "pending")}
          className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-600"
        >
          <option value="all">All Tasks</option>
          <option value="pending">Pending</option>
          <option value="completed">Completed</option>
        </select>
      </div>

      {/* Todos Table */}
      <table className="w-full">
        <thead className="w-full">
          <tr className="w-full flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md">
            <th>Task</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {todo_list.length > 0 ? (
            todo_list.map((task: Todo) => (
              <Task key={task.id} task={task} />
            ))
          ) : (
            <tr>
              <td colSpan={2} className="text-center py-4 text-gray-500">
                No tasks found
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
