
import { useState } from 'react';
import PerfectScrollbar from 'react-perfect-scrollbar';
import PropTypes from 'prop-types';
import { format } from 'date-fns';
import {
  Avatar,
  Box,
  Card,
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TablePagination,
  TableRow,
  Typography
} from '@mui/material';
import { getInitials } from '../../utils/get-initials';


import {materialMaster} from '../../../material-master';


export const MaterialListResults = ({ customers, ...rest }) => {


  const [selectedCustomerIds, setSelectedCustomerIds] = useState([]);
  const [limit, setLimit] = useState(10);
  const [page, setPage] = useState(0);

  const handleSelectAll = (event) => {
    let newSelectedCustomerIds;

    if (event.target.checked) {
      newSelectedCustomerIds = customers.map((customer) => customer.id);
    } else {
      newSelectedCustomerIds = [];
    }

    setSelectedCustomerIds(newSelectedCustomerIds);
  };

  const handleSelectOne = (event, id) => {
    const selectedIndex = selectedCustomerIds.indexOf(id);
    let newSelectedCustomerIds = [];

    if (selectedIndex === -1) {
      newSelectedCustomerIds = newSelectedCustomerIds.concat(selectedCustomerIds, id);
    } else if (selectedIndex === 0) {
      newSelectedCustomerIds = newSelectedCustomerIds.concat(selectedCustomerIds.slice(1));
    } else if (selectedIndex === selectedCustomerIds.length - 1) {
      newSelectedCustomerIds = newSelectedCustomerIds.concat(selectedCustomerIds.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelectedCustomerIds = newSelectedCustomerIds.concat(
        selectedCustomerIds.slice(0, selectedIndex),
        selectedCustomerIds.slice(selectedIndex + 1)
      );
    }

    setSelectedCustomerIds(newSelectedCustomerIds);
  };

  const handleLimitChange = (event) => {
    setLimit(event.target.value);
  };

  const handlePageChange = (event, newPage) => {
    setPage(newPage);
  };

  return (
    <Card {...rest}>
      <PerfectScrollbar>
        <Box sx={{ minWidth: 1050 }} style={{overflow:"scroll",height:"500px"}}>
          <Table stickyHeader={true} >
            <TableHead >
              <TableRow >
                {/* <TableCell padding="checkbox">
                  <Checkbox
                    checked={selectedCustomerIds.length === customers.length}
                    color="primary"
                    indeterminate={
                      selectedCustomerIds.length > 0
                      && selectedCustomerIds.length < customers.length
                    }
                    onChange={handleSelectAll}
                  />
                </TableCell> */}
                <TableCell>
                  material
                </TableCell>
                <TableCell>
                  material_9
                </TableCell>
                <TableCell>
                  material_7
                </TableCell>
                <TableCell>
                  mat_description
                </TableCell>
                <TableCell >
                  mat_description_eng
                </TableCell>
                <TableCell>
                  plant
                </TableCell>
                <TableCell>
                  planner
                </TableCell>
                <TableCell>
                  safety_stock
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {materialMaster.slice(0, limit).map((material) => (
                <TableRow
                  hover
                  key={material.material_7}
                  
                  
                  // selected={selectedCustomerIds.indexOf(customer.id) !== -1}
                >
                  {/* <TableCell padding="checkbox">
                    <Checkbox
                      checked={selectedCustomerIds.indexOf(customer.id) !== -1}
                      onChange={(event) => handleSelectOne(event, customer.id)}
                      value="true"
                    />
                  </TableCell> */}
                  <TableCell >
                    <Box
                      sx={{
                        // alignItems: 'center',
                        // display: 'flex',
                        // overflow:"scroll"
                      }}
                    >
                      {/* <Avatar
                        src={customer.avatarUrl}
                        sx={{ mr: 2 }}
                      >
                        {getInitials(customer.name)}
                      </Avatar> */}
                      <Typography
                        color="textPrimary"
                        variant="body1"
                      >
                        {material.material}
                      </Typography>
                    </Box>
                  </TableCell>
                  <TableCell>
                    {material.material_9}
                  </TableCell>
                  <TableCell>
                   {material.material_7}
                  </TableCell>
                  <TableCell>
                    {material.mat_description}
                  </TableCell>
                  <TableCell>
                    {material.mat_description_eng}
                  </TableCell>
                  <TableCell>
                    {material.plant}
                  </TableCell>
                  <TableCell align="center">
                    {material.planner}
                  </TableCell>
                  <TableCell align="center">
                  {material.safety_stock}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Box>
      </PerfectScrollbar>
      <TablePagination
        component="div"
        count={customers.length}
        onPageChange={handlePageChange}
        onRowsPerPageChange={handleLimitChange}
        page={page}
        rowsPerPage={limit}
        rowsPerPageOptions={[5, 10, 25]}
      />
    </Card>
  );
};

MaterialListResults.propTypes = {
  customers: PropTypes.array.isRequired
};
