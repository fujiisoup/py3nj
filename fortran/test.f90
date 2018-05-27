program main

  call test_drc3jj
  call test_drc3jj_int
  call test_drc3jj_vec
  call test_drc3jj_vec2
end program main


subroutine test_drc3jj
  implicit none
  double precision l2, l3, m2, m3, l1min, l1max
  integer ier
  double precision thrcof(10)

  l2 = 1.0
  l3 = 1.0
  m2 = 0.0
  m3 = 0.0
  call drc3jj(l2, l3, m2, m3, l1min, l1max, thrcof, 10, ier)
  print *, l1min, l1max
  print *, thrcof

  l2 = 0.5
  l3 = 1.0
  m2 = 0.0
  m3 = 0.0
  call drc3jj(l2, l3, m2, m3, l1min, l1max, thrcof, 10, ier)
  print *, l1min, l1max
  print *, thrcof
end subroutine test_drc3jj


subroutine test_drc3jj_int
  implicit none
  integer l2, l3, m2, m3, l1min, l1max
  integer ier
  double precision thrcof(10)

  l2 = 2
  l3 = 2
  m2 = 0
  m3 = 0
  call drc3jj_int(l2, l3, m2, m3, l1min, l1max, thrcof, 10, ier)
  print *, l1min, l1max
  print *, thrcof

  l2 = 18
  l3 = 0
  m2 = 10
  m3 = 0
  call drc3jj_int(l2, l3, m2, m3, l1min, l1max, thrcof, 10, ier)
  print *, l1min, l1max
  print *, thrcof
end subroutine test_drc3jj_int


subroutine test_drc3jj_vec
  implicit none
  integer l2(11), l3(11), m2(11), m3(11), nvec, ndim, ier
  double precision thrcof(11, 8)

  l2 = (/ 5, 0, 3, 3, 7, 9, 3, 5, 2, 4, 4/)
  l3 = (/ 0, 3, 2, 0, 7, 5, 9, 0, 2, 7, 7/)
  m2 = (/ 4, 0, 0, 1,-2,-6,-2, 4, 1, 2, 2/)
  m3 = (/ 0, 2, 0, 0, 6,-2, 0, 0, 1, 3, 3/)
  call drc3jj_vec(l2, l3, m2, m3, 11, thrcof, 8, ier)
  print *, thrcof
end subroutine test_drc3jj_vec

subroutine test_drc3jj_vec2
  implicit none
  integer l2(2), l3(2), m2(2), m3(2), nvec, ndim, ier
  double precision thrcof(2, 19)
  integer i

  l2 = (/ 18, 10/)
  l3 = (/ 0, 0/)
  m2 = (/ 10, 1/)
  m3 = (/ 0, 0/)

  do i=1, 4
    call drc3jj_vec(l2, l3, m2, m3, 2, thrcof, 19, ier)
    print *, ier, i
  enddo
end subroutine test_drc3jj_vec2
