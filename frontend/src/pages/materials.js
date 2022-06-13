import { Box, Container } from '@mui/material';
import { MaterialListResults } from '../components/material/material-list-results';
import { MaterialListToolbar } from '../components/material/material-list-toolbar';
import { DashboardLayout } from '../components/common/dashboard-layout';
import { customers } from '../__mocks__/customers';

const Customers = () => (
  <div style={{marginTop:"-4%"}}>
  
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 0
      }}
    >
      <Container maxWidth={false}>
        <MaterialListToolbar />
        <Box sx={{ mt: 0 }}>
          <MaterialListResults customers={customers} />
        </Box>
      </Container>
    </Box>
  </div>
);
Customers.getLayout = (page) => (
  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Customers;
