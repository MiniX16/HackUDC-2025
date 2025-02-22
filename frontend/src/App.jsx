import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IntroPage from "./pages/IntroPage";
import RecomendationPage from "./pages/RecomendationPage";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<IntroPage />} />
                <Route path="/recomendation" element={<RecomendationPage />} />
            </Routes>
        </Router>
    );
}

export default App;
