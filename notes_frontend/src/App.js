import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";
import './App.css';

import Header from './components/Header';
import NotesListPage from './scenes/NotesListPage';
import NotePage from "./scenes/NotePage";

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Header />
          <Route path="/" exact component={NotesListPage} />
          <Route path="/note/:id" component={NotePage} />
        </div>
      </div>
    </Router>
    
  );
};

export default App;
