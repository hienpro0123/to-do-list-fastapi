"use client";
import { CiSquareCheck } from "react-icons/ci";
import { Todo } from "../../types";
import { FiEdit, FiTrash2 } from "react-icons/fi";
import ToolTip from "./ToolTip";
import { Modal } from "./ui/Modal";
import toast from "react-hot-toast";
import { useState } from "react";
import { apiUrl } from "../lib/api";

export default function Task({ task }: { task: Todo }) {
  const [loading, setLoading] = useState(false);

  const handleStatus = async () => {
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
          content: task.content,
          is_completed: !task.is_completed,
        }),
      });

      const data = await response.json();
      if (response.ok && data.content) {
        toast.success("Status changed successfully");
        window.location.reload();
      } else {
        toast.error("Failed to update status");
      }
    } catch (error) {
      toast.error("Network error");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem("token");
      if (!token) {
        toast.error("Not authenticated");
        return;
      }

      const response = await fetch(apiUrl(`/todos/${task.id}`), {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();
      if (response.ok && data.message) {
        toast.success(data.message);
        window.location.reload();
      } else {
        toast.error("Failed to delete todo");
      }
    } catch (error) {
      toast.error("Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <tr className="flex justify-between items-center border-b border-gray-300 px-2 py-2">
      <td>{task.content}</td>
      <td className="flex gap-x-2">
        <ToolTip tool_tip_content="Mark as completed">
          <button onClick={handleStatus} disabled={loading}>
            <CiSquareCheck
              size={28}
              className={`${
                task.is_completed ? "text-green-500" : "text-gray-300"
              } ${loading ? "opacity-50" : ""}`}
            />
          </button>
        </ToolTip>

        <Modal title="Edit Task" Editing={true} task={task}>
          <FiEdit size={24} className="text-blue-500" />
        </Modal>

        <button onClick={handleDelete} disabled={loading}>
          <FiTrash2
            size={24}
            className={`text-red-600 ${loading ? "opacity-50" : ""}`}
          />
        </button>
      </td>
    </tr>
  );
}
