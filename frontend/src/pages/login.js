import Head from "next/head";
import { useRouter } from "next/router";
import { useFormik } from "formik";
import { useState } from "react";
import { Box, Button, Container, Grid, Link, TextField, Typography } from "@mui/material";
import { loginCall } from "src/utils/apihelper";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const router = useRouter();
  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
  });

  const submit = async () => {
    const body = new FormData();

    body.append("username", username);
    body.append("password", password);

    const LoginResponse = await loginCall(body);
    console.log("response", LoginResponse);

    localStorage.setItem("token", LoginResponse.access_token);
    localStorage.setItem("plannerId", username);
    router.push("/");
  };

  return (
    <>
      <Head>
        <title>BMW Material Planner</title>
        <link rel="icon" type="image/png" href="bmw_logo_PNG19714.png"></link>
      </Head>
      <Box
        component="main"
        sx={{
          alignItems: "center",
          display: "flex",
          flexGrow: 1,
          minHeight: "100%",
        }}
      >
        <Container maxWidth="sm">
          {/* <NextLink
            href="/"
            passHref
          >
            <Button
              component="a"
              startIcon={<ArrowBackIcon fontSize="small" />}
            >
              Dashboard
            </Button>
          </NextLink> */}
          <form onSubmit={formik.handleSubmit}>
            <Box sx={{ my: 3 }}>
              <Typography color="textPrimary" variant="h4">
                Sign in
              </Typography>
              <Typography color="textSecondary" gutterBottom variant="body2">
                Sign in on the internal platform
              </Typography>
            </Box>
            <Grid container spacing={3}>
              {/* <Grid
                item
                xs={12}
                md={6}
              >
                <Button
                  color="info"
                  fullWidth
                  startIcon={<FacebookIcon />}
                  onClick={formik.handleSubmit}
                  size="large"
                  variant="contained"
                >
                  Login with Facebook
                </Button>
              </Grid> */}
              {/* <Grid
                item
                xs={12}
                md={6}
              >
                <Button
                  fullWidth
                  color="error"
                  startIcon={<GoogleIcon />}
                  onClick={formik.handleSubmit}
                  size="large"
                  variant="contained"
                >
                  Login with Google
                </Button>
              </Grid> */}
            </Grid>
            <Box
              sx={{
                pb: 1,
                pt: 3,
              }}
            >
              <Typography align="center" color="textSecondary" variant="body1">
                {/* or login with email address */}
              </Typography>
            </Box>
            <TextField
              // error={Boolean(formik.touched.email && formik.errors.email)}
              fullWidth
              helperText={formik.touched.email && formik.errors.email}
              label="User name"
              margin="normal"
              name="email"
              onBlur={formik.handleBlur}
              onChange={(e) => {
                setUsername(e.target.value);
              }}
              type="text"
              value={username}
              variant="outlined"
            />
            <TextField
              // error={Boolean(formik.touched.password && formik.errors.password)}
              fullWidth
              helperText={formik.touched.password && formik.errors.password}
              label="Password"
              margin="normal"
              name="password"
              onBlur={formik.handleBlur}
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              type="password"
              value={password}
              variant="outlined"
            />
            <Box sx={{ py: 2 }}>
              <Button
                color="primary"
                disabled={false}
                fullWidth
                size="large"
                type="submit"
                variant="contained"
                onClick={submit}
              >
                Sign In Now
              </Button>
            </Box>
            {/* <Typography
              color="textSecondary"
              variant="body2"
            >
              Don&apos;t have an account?
              {' '}
              <NextLink
                href="/register"
              >
                <Link
                  to="/register"
                  variant="subtitle2"
                  underline="hover"
                  sx={{
                    cursor: 'pointer'
                  }}
                >
                  Sign Up
                </Link>
              </NextLink>
            </Typography> */}
          </form>
        </Container>
      </Box>
    </>
  );
};

export default Login;
