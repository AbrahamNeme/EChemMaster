import React, {Component} from 'react';
import { render } from "react-dom";
import PeriodicTable from './PeriodicTable';
import ElementDetail from './ElementDetail';

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="center">
        <PeriodicTable />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

