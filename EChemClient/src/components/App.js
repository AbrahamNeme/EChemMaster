import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { render } from "react-dom";
import PeriodicTable from './PeriodicTable';
import ElementDetail from './ElementDetail';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" component={PeriodicTable} />
        <Route path="/element/:symbol" component={ElementDetail} />
      </Routes>
    </Router>
  );
}
//export default App;

const appDiv = document.getElementById("app");
render(<App/>, appDiv);

