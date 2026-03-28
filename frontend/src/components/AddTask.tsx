"use client";
import { useRef, useState } from "react";
import toast from "react-hot-toast";
import SubmitButton from "./SubmitButton";
import { apiUrl } from "../lib/api";

export default function AddTask() {
  const ref = useRef<HTMLFormElement>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData(e.currentTarget);
    const content = formData.get("add_task") as string;

    try {
      const token = localStorage.getItem("token");
      if (!token) {
        toast.error("Not authenticated. Please log in.");
        setLoading(false);
        return;
      }

      const response = await fetch(apiUrl("/todos/"), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ content }),
      });

      const data = await response.json();
      
      if (response.ok && data.content) {
        ref.current?.reset();
        toast.success("Todo added successfully");
        // Refresh the page to show new todo
        window.location.reload();
      } else {
        toast.error(data.detail || "Failed to add todo");
      }
    } catch (error) {
      console.error("Error adding todo:", error);
      toast.error("Network error - please check if backend is running");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      ref={ref}
      onSubmit={handleSubmit}
      className="flex flex-col justify-between items-center gap-x-4 w-full"
    >
      <input
        type="text"
        placeholder="Add Task here"
        minLength={3}
        maxLength={54}
        required
        name="add_task"
        className="w-full px-2 py-1 border border-gray-100 rounded-md"
        disabled={loading}
      />
      <SubmitButton disabled={loading} />
    </form>
  );
}
