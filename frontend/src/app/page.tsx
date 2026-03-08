"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import TodoTable from "@/components/TodoTable";
import { Modal } from "@/components/ui/Modal";
import { Button } from "@/components/ui/button";
import LogoutButton from "@/components/LogoutButton";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      router.push("/login");
    }
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    router.push("/login");
  };

  return (
    <main className="max-w-5xl mx-auto mt-8">
      {/* Header */}
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">My Tasks</h1>
        <LogoutButton />
      </div>

      {/* Add Task Section */}
      <section>
        <Modal title="Add New Task" Adding={true}>
          <Button className="w-full bg-teal-600 px-2 py-1 text-white uppercase text-lg">
            Add Task
          </Button>
        </Modal>
      </section>

      {/* Todo Table */}
      <section className="mt-4">
        <TodoTable />
      </section>
    </main>
  );
}