"use client";
import { Todo } from "../../types";
import SubmitButton from "./SubmitButton";
import { useState } from "react";
import toast from "react-hot-toast";
import { apiUrl } from "../lib/api";

export default function EditTask({ task }: { task: Todo }) {
  const [value, setValue] = useState(task.content);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    try {
      const token = localStorage.getItem("token");
      if (!token) {
        toast.error("Not authenticated");
        return;
      }

      const response = await fetch(apiUrl(`/todos/${task.id}`), {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          content: value,
          is_completed: task.is_completed,
        }),
      });

      const data = await response.json();
      if (response.ok && data.content) {
        toast.success("Todo edited successfully");
        window.location.reload();
      } else {
        toast.error(data.detail || "Not found");
      }
    } catch (error) {
      toast.error("Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col justify-between items-center gap-x-4 w-full"
    >
      <input
        onChange={handleChange}
        type="text"
        minLength={3}
        maxLength={54}
        required
        name="edit_task"
        value={value}
        className="w-full px-2 py-1 border border-gray-100 rounded-md"
        disabled={loading}
      />
      <SubmitButton disabled={loading} />
    </form>
  );
}
