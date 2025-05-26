import React from "react";

function TopicsPage() {
  return (
    <div>
      <h2>Web Development Concepts</h2>
      <nav class="local-articles">
        <a id="about-servers" href="#about-web-servers">
          About Web Servers
        </a>
        <a id="frontend" href="#frontend-design">
          Frontend Design
        </a>
        <a id="images" href="#optimizing-images">
          Optimizing Images
        </a>
        <a id="css" href="#cascading-stylesheets">
          Cascading Stylesheets
        </a>
        <a id="ctrlforms" href="#forms">
          Forms
        </a>
        <a id="expressapp" href="#express">
          Express
        </a>
        <a id="javascript" href="#js">
          JavaScript
        </a>
        <a id="dom-express" href="#dom">
          DOM
        </a>
      </nav>
      <article id="about-web-servers">
        <h3>About Web Servers</h3>
        <p>
          An index.html file is an Apache web server's default page and often
          the homepage for other servers. To create one,
          <strong>make a new folder</strong> and open it in VS Code.
          <strong>Create a directory file</strong> named index.html.{" "}
          <strong>Add necessary HTML tags</strong>: html, head, title, body, and
          an optional meta tag to disallow bot crawling.{" "}
          <strong>Open the file</strong>
          in-browser, then the Network tab in Web Dev/Inspect tools.{" "}
          <strong>Disable the cache</strong> to prevent older page versions from
          interfering with edits. The Network tab shows HTTP requests and
          responses.
        </p>
        <p>
          For a local index.html file, the Inspector shows a local path for a{" "}
          <strong>request URL</strong>. It also shows a GET request, used to
          send or receive resources. A<strong>status code</strong> (200) shows a
          reason phrase of OK, indicating a successful request. The{" "}
          <strong>referrer policy</strong> is strict-origin-when-cross-origin.
          It sends the origin, or URL scheme, and mitigates data leakage. The
          <strong>content-type</strong> shows an HTML request. The
          <strong>request headers</strong> describe system and browser
          information.
        </p>
        <p>
          The Inspector shows a favicon.ico image for the hosted index.html
          without any manual actions. Favicon images are separate resources not
          included in HTML code. Instead, they're often requested by default in
          browsers. It's not uncommon for developers to include them in
          websites' root directories. If one is unavailable, browsers may even
          display another default image. Main.css and main.js files are
          different, as they're integrated resources that HTML code calls.
        </p>
        <p>
          The hosted index.html file shows more fields in Network, like an IP{" "}
          <strong>remote address</strong>. There is also Apache web server
          information. The page has an
          <strong>accept-range</strong> in bytes for partial requests to
          conserve bandwidth. The file uses a gzip compression algorithm for{" "}
          <strong>content encoding</strong>.<strong>Content-Length</strong> is
          875 total bytes for the recourse. An <strong>entity tag</strong> is
          present for web cache validation. The site's{" "}
          <strong>Keep-Alive</strong>
          connection shows a 15-second timeout. <strong>Sec-Fetch-Mode</strong>
          is navigate for HTML pages. <strong>Upgrade-Insecure-Requests</strong>
          shows a server signal for encryption and authentication.
        </p>
        <p>
          The index.html file's URL scheme is <strong>HTTPS</strong>, which
          encrypts information sent and received. Today, HTTPS protocols use the
          cryptographic protocol Transport Layer Security. The{" "}
          <strong>subdomain</strong>
          web.engr is the Oregon State University College of Engineering. It
          resides under oregonstate.edu, the school's
          <strong>hostname</strong> domain. <strong>Resource paths</strong>{" "}
          allow web clients to access specific resources. This URL's path,
          ~blanform/a1-blanform/, leads to this CS 290 student's parent
          directory.
        </p>
      </article>
      <article id="frontend-design">
        <h3>Frontend Design</h3>
        <p>
          Frontend web design entails the user experience. A website or app's
          visual design and GUI requires
          <strong>color</strong>, <strong>font</strong>, and
          <strong>typography</strong> schemes. It also needs
          <strong>photography</strong>, <strong>icon</strong>, and
          <strong>illustration</strong> schemes. A worthwhile user experience
          requires a <strong>navigation</strong> system to visit other pages.
          Design trends change year-to-year, but these qualities are always
          necessary. Without them, a user base could dwindle.
        </p>
        <p>A website's usability follows five Es:</p>
        <dl>
          <dt>
            <strong>Effective</strong>
          </dt>
          <dd>The website helps users meet goals with accuracy.</dd>
          <dt>
            <strong>Efficient</strong>
          </dt>
          <dd>
            The platform helps users complete tasks in the least possible steps.
          </dd>
          <dt>
            <strong>Easy to navigate</strong>
          </dt>
          <dd>
            New users especially must immediately understand how to use the
            site.
          </dd>
          <dt>
            <strong>Error-free</strong>
          </dt>
          <dd>
            There are two As for user issues: accessibility and availability.
            Developers must observe and understand the most common errors and
            roadblocks encountered.
          </dd>
          <dt>
            <strong>Enjoyable to use/engaging</strong>
          </dt>
          <dd>
            Technically, that's a sixth E, but the two are synonymous. Websites
            should fit an audience's unique needs in content and design.
          </dd>
        </dl>
        <p>
          Any missing E wastes time, limits productivity, and frustrates users.
        </p>
        <p>
          Page layout tags organize content into sections. Aesthetics change
          with CSS code, but the tags help search engine robots and screen
          readers navigate pages. The
          <strong>&lt;header&gt;</strong>
          element often has names and slogans, while
          <strong>&lt;footer&gt;</strong>
          holds legal and contact information. The
          <strong>&lt;nav&gt;</strong> tag takes users to other pages. The main
          content, <strong>&lt;main&gt;</strong>, has
          <strong>&lt;section&gt;</strong> tags grouping by motif (i.e., how
          newspapers have different sections like crime or sports). Sections
          contain specific
          <strong>&lt;article&gt;</strong> elements marked by ID selectors for
          anchors and internal jumps. An
          <strong>&lt;aside&gt;</strong> element is a sidebar with unrelated
          content — e.g., media via
          <strong>&lt;figure&gt;</strong> or quotes via
          <strong>&lt;blockquote&gt;</strong>.
        </p>
        <p>
          Developers link sections or pages with
          <strong>anchor</strong> tags. Hyperlinks go in
          <strong>&lt;a&gt;</strong> tags, describing where users might
          navigate. The <strong>href</strong>
          attribute specifies the exact URL — not necessarily external. The{" "}
          <strong>&lt;a href=" "&gt;</strong> command can link to a place
          internally with an ID preceding a hash (#) symbol.
        </p>
      </article>
      <article id="optimizing-images">
        <h3>Optimizing Images</h3>
        <p>
          Web images have six major specifications.{" "}
          <strong>Descriptive file names</strong> improve SEO.
          <strong>Small file sizes</strong> reduce load times, and lossless
          compression doesn't degrade quality compared to lossy.{" "}
          <strong>Exact dimensions</strong> reduce loading, as does{" "}
          <strong>file format</strong> — e.g., PNGs have true transparency so
          are best for line art. <strong>Reduced resolution</strong> helps
          because varying image sizes are a relatively new standard. The correct
          <strong>color mode</strong> suits file types with specific palette
          limitations.
        </p>
        <p>
          <strong>Line art</strong> files should be GIF, PNG, or SVG format.
          GIFs have eight-bit transparency and anti-aliased edges, while PNGs
          have true alpha transparency. SVGs are good for two-dimensional,
          interactive, or animated images with XML declaration.{" "}
          <strong>Photography</strong> needs JPG format or WebP, which have
          transparency with an alpha channel.
        </p>
      </article>
      <article id="cascading-stylesheets">
        <h3>Cascading Stylesheets</h3>
        <p>
          Stylesheets override content appearance and behavior for predefined
          HTML code, making it more usable, readable, and legible. External
          sheets make global changes — ideal for designing entire websites.
          However, style rules use a cascading method, from least to most
          authority — linked external sheets, imported external sheets, embedded
          sheets, then inline styling.
        </p>
        <p>
          There are five ways to incorporate styles in websites, beginning with
          external CSS rules that are defined with .css and &lt;link&gt;ed a
          global &lt;head&gt;. External sheets are preferred, but other methods
          are embedded in HTML and JavaScript. Those four methods are embedded{" "}
          <strong>style tags</strong>, <strong>inline</strong> an element, or by{" "}
          <strong>regular JavaScript</strong> or{" "}
          <strong>JavaScript template literals</strong>.
        </p>
      </article>
      <article id="forms">
        <h3>Forms</h3>
        <p>
          Accessibility is an ADA-required feature for US government websites,
          and there are six key goals. Sites must{" "}
          <strong>give clear instructions</strong> for forms and labels. They
          must also <strong>explain to users</strong> and data-collection
          purposes and indicate required fields. Users need{" "}
          <strong>autofocus on the first field</strong>, and developers must
          implement <strong>form-filling by keyboard</strong>. Also,{" "}
          <strong>tab-indexing</strong> shows correct form sequence, and
          validation messages must be <strong>screen-readable</strong>.
        </p>
        <p>
          The major tags are <strong>form</strong> tags with action attributes
          specifying destination and and HTTP methods for POST (data sent in the
          body) and GET (data sent in the URL). <strong>Label</strong> tags
          explain data entry purposes. The for="" attribute should match the
          id="" for <strong>input</strong>, which acquires user data in a form
          with type="" and name="" attributes to alter display and organize data
          by form location, respectively. <strong>Fieldset</strong> and{" "}
          <strong>legend</strong> tags organize form controls, with the latter
          including informative prompts. <strong>Button</strong> elements carry
          out the action="" route.
        </p>
        <p>
          The fieldset's default gray should be another color, type, and width,
          with margins and padding for extra space. Color and larger font-size
          help legend readability overall. Display labels in block-style for
          less clutter. Inherit font attributes and slightly increase font size
          for input, button, textarea, and select tags; don't forget padding,
          also. Implement a different background color and border for focus
          (i.e., the current field) and required fields.
        </p>
      </article>
      <article id="express">
        <h3>Express</h3>
        <p>
          <strong>Node.js</strong> is a runtime environment with libraries for
          web development. The <strong>npm</strong> command-line utility helps
          install and publish Node packages. <strong>Express</strong> is a
          framework that provides various common APIs. It allows the ability to
          acquire, publish, and delete data while also amending ports and routes
          and serving static files.
        </p>
      </article>
      <article id="js">
        <h3>JavaScript</h3>
        <p>
          JavaScript has several <strong>data types</strong>: numbers, booleans,
          strings, symbols, and objects, as well as null and undefined special
          values.
        </p>
        <p>
          <strong>Objects</strong> are name-value pairs, or properties for
          creating, reading, updating, and deleting (CRUD).{" "}
          <strong>Arrays</strong> are zero-indexed objects in square brackets.
          The values are any type, including objects, but the code returns
          undefined-type if no element. <strong>JSON</strong> (JavaScript Object
          Notation) exchanges data between applications, independent of all
          languages. JSON can map objects to strings or vice-versa. Two main
          methods are <code>JSON.stringify()</code> that creates JSON strings
          from JavaScript objects or <code>JSON.parse()</code>, which creates
          JavaScript objects from JSON strings.
        </p>
        <p>
          JavaScript <strong>conditionals</strong> and <strong>loops</strong>{" "}
          evaluate conditions or repeat code blocks until a met condition,
          respectively. These all meet necessary functions for{" "}
          <strong>object-oriented programming</strong> (OOP), a paradigm
          centered around object-creation and -alteration in programming.
          Classes and functions help organize this logic while setting behavior.{" "}
          <strong>Functional programming</strong> entails functions as
          "first-class" values — i.e., they can assign to variables and define
          behavior overall.
        </p>
      </article>
      <article id="dom">
        <h3>DOM</h3>
        <p>
          JavaScript and Express are efficient for updating a site's{" "}
          <strong>Document Object Model</strong> due to dynamic and responsive
          UI. With DOM manipulation — e.g., innerHTML — developers can add,
          change, or remove content without requiring a static-page reload.
          JavaScript also helps fetch API data more efficiently.
        </p>
      </article>
    </div>
  );
}

export default TopicsPage;
