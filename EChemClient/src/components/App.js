import React, { Component } from "react";
import { render } from "react-dom";

export default function App(props) {
    return (
        <div>
            <h1> This is the App.js react component!</h1>
            <h2> :) </h2>
        </div>
    );
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);