import React, { useState } from "react";

const Register = () => {
  const [form, setForm] = useState({
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  const handleChange = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await fetch("/djangoapp/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
  };

  return (
    <div className="register-page">
      <h1>Sign-up</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input id="username" name="username" type="text" placeholder="Username" value={form.username} onChange={handleChange} />

        <label htmlFor="firstName">First Name</label>
        <input id="firstName" name="firstName" type="text" placeholder="First Name" value={form.firstName} onChange={handleChange} />

        <label htmlFor="lastName">Last Name</label>
        <input id="lastName" name="lastName" type="text" placeholder="Last Name" value={form.lastName} onChange={handleChange} />

        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} />

        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} />

        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
