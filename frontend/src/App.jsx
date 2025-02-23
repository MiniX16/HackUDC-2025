import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IntroPage from "./pages/IntroPage";
import RecomendationPage from "./pages/RecomendationPage";
import OutfitRecommendation from "./pages/OutfitRecommendation";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<IntroPage />} />
                <Route path="/recomendation" element={<RecomendationPage />} />
                <Route path="/outfit-recommendation/" element={<OutfitRecommendation />} />
            </Routes>
        </Router>
    );
}

export default App;
