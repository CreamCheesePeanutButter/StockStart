import {
  Route,
  createHashRouter,
  createRoutesFromElements,
  BrowserRouter,
  Routes,
  RouterProvider,
} from "react-router-dom";

import RootLayout from "./layout/rootlayout";
import Homepage from "./pages/homepage.tsx";
import LoginPage from "./pages/loginpage.tsx";
import AboutPage from "./pages/aboutpage.tsx";
function App() {
  const router = createHashRouter(
    createRoutesFromElements(
      <Route path="/" element={<RootLayout />}>
        <Route index element={<Homepage />} />
      </Route>,
    ),
  );

  return (
    <>
      <RouterProvider router={router} />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}
export default App;
