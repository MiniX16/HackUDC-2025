import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IntroPage from "./pages/IntroPage";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<IntroPage />} />
            </Routes>
        </Router>
    );
}

export default App;
