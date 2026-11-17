import { useEffect, useState } from "react";
import axios from "axios";

interface Employee {
  id: number;
  name: string;
  email: string;
  role: string;
  created_at: string;
}

const API = "http://127.0.0.1:8000/employees";
const emptyForm = { name: "", email: "", role: "" };

export default function App() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [form, setForm] = useState(emptyForm);
  const [editingId, setEditingId] = useState<number | null>(null); // null  =  adding

  const load = async () => {
    const res = await axios.get<Employee[]>(API);
    setEmployees(res.data);
  };

  useEffect(() => {
    load();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); 
    if (editingId === null) {
      await axios.post(API, form);
    } else {
      await axios.put(`${API}/${editingId}`, form);
    }
    setForm(emptyForm);
    setEditingId(null);
    load(); 
  };

  const startEdit = (emp: Employee) => {
    setEditingId(emp.id);
    setForm({ name: emp.name, email: emp.email, role: emp.role });
  };

  // delete button
  const remove = async (id: number) => {
    if (!confirm("Delete this employee?")) return;
    await axios.delete(`${API}/${id}`);
    load();
  };

  return (
    <div className="container">
      <h1>Employee Directory</h1>

      <form onSubmit={handleSubmit} className="form">
        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} required />
        <input name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} required />
        <input name="role" placeholder="Role" value={form.role} onChange={handleChange} required />
        <button type="submit">{editingId === null ? "Add" : "Save"}</button>
        {editingId !== null && (
          <button
            type="button"
            className="gray"
            onClick={() => {
              setEditingId(null);
              setForm(emptyForm);
            }}
          >
            Cancel
          </button>
        )}
      </form>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Role</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id}>
              <td>{emp.name}</td>
              <td>{emp.email}</td>
              <td>{emp.role}</td>
              <td>
                <button onClick={() => startEdit(emp)}>Edit</button>{" "}
                <button className="red" onClick={() => remove(emp.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
          {employees.length === 0 && (
            <tr>
              <td colSpan={4} className="empty">
                No employees yet
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
