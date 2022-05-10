<template>
          <div class="col-sm-auto bg-light sticky-top">
          <div
            class="d-flex flex-sm-column flex-row flex-nowrap bg-light align-items-center sticky-top"
          >
            <a
              href="/"
              class="d-block p-3 link-dark text-decoration-none"
              title=""
              data-bs-toggle="tooltip"
              data-bs-placement="right"
              data-bs-original-title="Icon-only"
            >
              <MailIcon class="icon" />
            </a>
            <ul
              class="nav nav-pills nav-flush flex-sm-column flex-row flex-nowrap mb-auto mx-auto text-center justify-content-between w-100 px-3 align-items-center"
            >
              <li class="nav-item">
                <a
                  href="#"
                  class="nav-link py-3 px-2"
                  title=""
                  data-bs-toggle="tooltip"
                  data-bs-placement="right"
                  data-bs-original-title="Home"
                >
                  <InboxIcon class="icon" /> Inbox
                </a>
              </li>

              <li>
                <a
                  href="#"
                  class="nav-link py-3 px-2"
                  title=""
                  data-bs-toggle="tooltip"
                  data-bs-placement="right"
                  data-bs-original-title="Dashboard"
                >
                  <StarIcon class="icon" /> Stared Mails
                </a>
              </li>
              <li class="nav-item">
                <a
                  href="#"
                  class="nav-link py-3 px-2"
                  title=""
                  data-bs-toggle="tooltip"
                  data-bs-placement="right"
                  data-bs-original-title="Home"
                >
                  <InboxIcon class="icon" /> Deleted Mails
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="nav-link py-3 px-2"
                  title=""
                  data-bs-toggle="tooltip"
                  data-bs-placement="right"
                  data-bs-original-title="Customers"
                >
                  <UserAddIcon class="icon" /> Add User
                </a>
              </li>
            </ul>
          </div>
        </div>
</template>

<script>
import {
  MailIcon,
  StarIcon,
  InboxIcon,
  UserAddIcon,
} from "@heroicons/vue/outline";
export default {
  components: { MailIcon, StarIcon, InboxIcon, UserAddIcon },
};
</script>

<style>

</style>