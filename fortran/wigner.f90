subroutine drc3jj_int(two_l2, two_l3, two_m2, two_m3, l1min, l1max, &
                      thrcof, ndim, ier)
! evaluate wigner's 3j symbol
  implicit none
  integer two_l2, two_l3, two_m2, two_m3, ndim, ier, l1min, l1max
  double precision l1min_d, l1max_d
  double precision thrcof(ndim)

  call drc3jj(0.5D0 * two_l2, 0.5D0 * two_l3, 0.5D0 * two_m2, 0.5D0 * two_m3, &
              l1min_d, l1max_d, thrcof, ndim, ier)
  l1min = nint(l1min_d*2)
  l1max = nint(l1max_d*2)

end subroutine drc3jj_int


subroutine drc3jj_vec(two_l2, two_l3, two_m2, two_m3, nvec, thrcof, ndim, ier)
  ! evaluate wigner's 3j symbol with vectorized input
  implicit none
  integer nvec, ier, ndim
  integer two_l2(nvec), two_l3(nvec), two_m2(nvec), two_m3(nvec), l1min, l1max
  double precision, dimension(nvec, ndim) :: thrcof
  double precision, dimension(nvec, ndim) :: thrcof_tmp
  double precision l2(nvec), l3(nvec), m2(nvec), m3(nvec)
  integer :: indexes(nvec)
  integer :: indexes_max
  integer, dimension(nvec) :: ier_v
  double precision :: l1min_d(nvec), l1max_d(nvec)
  integer i, j, dl
  logical is_new

  indexes_max = 0
  indexes(:) = -1
  l1min_d(:) = 0
  l1max_d(:) = 0
  thrcof(:, :) = 0
  thrcof_tmp(:, :) = 0
  ier = 0

  do i=1, nvec
    is_new = .true.
    ! if invalid, skip it
    if (mod(two_l2(i)+abs(two_m2(i)), 2)==1) then
      is_new = .false.
    elseif (mod(two_l3(i)+abs(two_m3(i)), 2)==1) then
      is_new = .false.
    elseif (mod(two_l2(i)+two_l3(i), 2)==1) then
      is_new = .false.
    elseif (max(abs(two_l2(i)-two_l3(i)), abs(two_m2(i) + two_m3(i))) &
            > (two_l2(i) + two_l3(i))) then
      is_new = .false.
    else
      do j=1, i-1
        ! if there is duplicate input, we skip this
        if (two_l2(i)==two_l2(j) .and. two_l3(i)==two_l3(j)) then
          if (two_m2(i)==two_m2(j) .and. two_m3(i)==two_m3(j)) then
            indexes(i) = indexes(j)
            is_new=.false.
            exit
          endif
        endif
      enddo
    endif
    if (is_new) then
      ! new data
      indexes_max=indexes_max+1
      l2(indexes_max) = 0.5D0 * two_l2(i)
      l3(indexes_max) = 0.5D0 * two_l3(i)
      m2(indexes_max) = 0.5D0 * two_m2(i)
      m3(indexes_max) = 0.5D0 * two_m3(i)
      indexes(i)=indexes_max
    endif
  enddo

  ! core part
  !$omp parallel
  !$omp do
  do i=1, indexes_max
    call drc3jj(l2(i), l3(i), m2(i), m3(i), l1min_d(i), l1max_d(i), &
                thrcof_tmp(i, :), ndim, ier_v(i))
  enddo
  !$omp end do
  !$omp end parallel
  ! end of core part

  do i=1, indexes_max
    if (ier_v(i) > 0) then
      ier = ier_v(i)
      exit
    end if
  end do

  do i=1, nvec
    if (indexes(i) .ge. 0) then
      l1min = nint(real(l1min_d(indexes(i))) * 2)
      l1max = nint(real(l1max_d(indexes(i))) * 2)
      if (l1max > ndim) l1max = ndim
      dl = (l1max-l1min)/2+1
      thrcof(i, l1min+1:l1max+1:2) = thrcof_tmp(indexes(i), :dl)
    endif
  enddo

  return
end subroutine drc3jj_vec
