
const API_BASE = "http://127.0.0.1:5000";

const options = [
    { label: "Never", value: 0 },
    { label: "Rarely", value: 1 },
    { label: "Sometimes", value: 2 },
    { label: "Often", value: 3 },
    { label: "Always", value: 4 }
];

const categoryQuestions = {
    profile_visibility: {
        name: "Profile Visibility",
        questions: [
            "Is your profile visible to everyone?",
            "Can strangers view your profile information?",
            "Are your posts visible to the public?",
            "Have you reviewed your profile privacy settings?"
        ]
    },
    personal_information: {
        name: "Personal Information",
        questions: [
            "Do you publicly share your phone number?",
            "Do you share your email address publicly?",
            "Do you reveal personal details such as your birthday?",
            "Do your profiles reveal information about your family?"
        ]
    },
    location_privacy: {
        name: "Location Privacy",
        questions: [
            "Do you share your live location publicly?",
            "Do you post your location while you are still there?",
            "Do your posts reveal your home or workplace address?",
            "Do you publicly share your travel plans before leaving?"
        ]
    },
    posts_content: {
        name: "Posts and Content",
        questions: [
            "Do your posts reveal sensitive personal details?",
            "Do your photos contain private information in the background?",
            "Do you share content without checking its privacy implications?",
            "Do you leave old public posts containing personal information?"
        ]
    },
    friends_followers: {
        name: "Friends and Followers",
        questions: [
            "Do you accept follow requests from people you do not know?",
            "Do you allow unknown people to view your content?",
            "Do you regularly check your followers list?",
            "Can strangers easily contact you through your profile?"
        ]
    },
    tagging_mentions: {
        name: "Tagging and Mentions",
        questions: [
            "Can people tag you without your approval?",
            "Do you allow tagged posts to appear on your profile automatically?",
            "Do you review posts that mention you?",
            "Can other people identify your location through tags?"
        ]
    },
    account_security: {
        name: "Authentication and Account Security",
        questions: [
            "Do you reuse passwords across multiple accounts?",
            "Do you use weak or easy-to-guess passwords?",
            "Have you left two-factor authentication disabled?",
            "Do you stay signed in on shared or public devices?"
        ]
    },
    third_party_apps: {
        name: "Third-Party Applications",
        questions: [
            "Have you connected apps that you no longer use?",
            "Do you grant apps permissions without reviewing them?",
            "Do you use social login on unfamiliar websites?",
            "Have you left unnecessary third-party app access enabled?"
        ]
    },
    messaging_safety: {
        name: "Messaging and Social Engineering",
        questions: [
            "Do you open unexpected links from unknown accounts?",
            "Do you respond to suspicious messages asking for information?",
            "Do you share verification codes with other people?",
            "Do you trust messages claiming to be from support without verifying them?"
        ]
    },
    digital_footprint: {
        name: "Digital Footprint",
        questions: [
            "Have you left old public posts containing personal details?",
            "Do you rarely review your online presence?",
            "Is personal information about you publicly searchable?",
            "Do you ignore old accounts that may expose your information?"
        ]
    }
};

const categoryKeys = Object.keys(categoryQuestions);

const riskColors = {
    LOW: "#5de4c7",
    MODERATE: "#83a8ff",
    HIGH: "#ffbf69",
    CRITICAL: "#ff7185"
};

const questionsContainer = document.getElementById("questions");
const form = document.getElementById("assessment-form");
const countLabel = document.getElementById("question-count");
const message = document.getElementById("message");
const submitButton = document.getElementById("submit-button");

const allQuestions = [];

categoryKeys.forEach(key => {
    const category = categoryQuestions[key];

    const heading = document.createElement("h2");
    heading.className = "category-heading";
    heading.textContent = category.name;
    questionsContainer.appendChild(heading);

    category.questions.forEach(question => {
        allQuestions.push({ key, question });
    });
});

allQuestions.forEach((item, index) => {
    const section = document.createElement("div");
    section.className = "question";

    const heading = document.createElement("h3");
    heading.textContent =
        `${String(index + 1).padStart(2, "0")}. ${item.question}`;

    const optionGroup = document.createElement("div");
    optionGroup.className = "options";

    options.forEach(option => {
        const label = document.createElement("label");
        label.className = "option";

        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = `question-${index}`;
        radio.value = option.value;
        radio.required = true;
        radio.addEventListener("change", updateCount);

        const text = document.createElement("span");
        text.textContent = option.label;

        label.append(radio, text);
        optionGroup.appendChild(label);
    });

    section.append(heading, optionGroup);
    questionsContainer.appendChild(section);
});

function updateCount() {
    const answered = allQuestions.filter((_, index) =>
        form.querySelector(
            `input[name="question-${index}"]:checked`
        )
    ).length;

    countLabel.textContent =
        `${answered} / ${allQuestions.length} answered`;
}

function getRiskLevel(score) {
    if (score <= 20) return "LOW";
    if (score <= 40) return "MODERATE";
    if (score <= 70) return "HIGH";
    return "CRITICAL";
}

function renderCategoryCards(categories) {
    const container = document.getElementById("category-cards");
    container.replaceChildren();

    categoryKeys.forEach(key => {
        const category = categories[key];
        if (!category) return;

        const score = category.risk_score;
        const level = category.risk_level || getRiskLevel(score);
        const color = riskColors[level];

        const card = document.createElement("div");
        card.className = "category-card";

        const top = document.createElement("div");
        top.className = "category-card-top";

        const name = document.createElement("strong");
        name.textContent = category.category_name;

        const value = document.createElement("span");
        value.className = "category-score";
        value.style.color = color;
        value.textContent = `${score}/100`;

        top.append(name, value);

        const bar = document.createElement("div");
        bar.className = "category-bar";

        const fill = document.createElement("div");
        fill.className = "category-bar-fill";
        fill.style.width = `${score}%`;
        fill.style.backgroundColor = color;

        bar.appendChild(fill);

        const label = document.createElement("span");
        label.className = "category-level";
        label.style.color = color;
        label.textContent = `${level} RISK`;

        card.append(top, bar, label);
        container.appendChild(card);
    });
}

function renderRecommendations(recommendations, overallLevel) {
    const list = document.getElementById("recommendations");
    list.replaceChildren();

    if (recommendations?.length) {
        recommendations.forEach(item => {
            addRecommendation(
                list,
                `${item.category} (${item.risk_score}/100): ${item.recommendation}`
            );
        });
    } else {
        addRecommendation(
            list,
            "Continue reviewing your privacy settings regularly."
        );
    }

    const advice = {
        LOW: "Maintain good privacy habits and review your settings regularly.",
        MODERATE: "Review profile visibility, app permissions and public information.",
        HIGH: "Prioritize reducing public personal information and improving security.",
        CRITICAL: "Promptly review exposed information, account access and security settings."
    };

    addRecommendation(list, `Overall guidance: ${advice[overallLevel]}`);
}

function addRecommendation(list, text) {
    const item = document.createElement("li");
    item.textContent = text;
    list.appendChild(item);
}

form.addEventListener("submit", async event => {
    event.preventDefault();

    const answers = allQuestions.map((_, index) => {
        const selected = form.querySelector(
            `input[name="question-${index}"]:checked`
        );
        return selected ? Number(selected.value) : null;
    });

    if (answers.some(answer => answer === null)) {
        message.textContent = "Please answer all questions.";
        return;
    }

    const categoryAnswers = {};

    categoryKeys.forEach(key => {
        categoryAnswers[key] = [];
    });

    allQuestions.forEach((item, index) => {
        categoryAnswers[item.key].push(answers[index]);
    });

    submitButton.disabled = true;
    message.textContent = "Analyzing your privacy risk...";

    try {
        const categoryResponse = await fetch(
            `${API_BASE}/api/categories`,
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ categories: categoryAnswers })
            }
        );

        const categoryData = await categoryResponse.json();

        if (!categoryResponse.ok) {
            throw new Error(
                categoryData.error || "Category analysis failed."
            );
        }

        const categories = categoryData.categories;
        const scores = Object.values(categories).map(
            item => item.risk_score
        );

        const overallScore = Math.round(
            scores.reduce((sum, score) => sum + score, 0) / scores.length
        );

        const overallLevel = getRiskLevel(overallScore);

        // Save the overall assessment in the existing database.
        const saveResponse = await fetch(`${API_BASE}/api/assess`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ answers,
    categories: categoryAnswers })
        });

        const saveData = await saveResponse.json();

        if (!saveResponse.ok) {
            throw new Error(saveData.error || "Could not save assessment.");
        }

        const color = riskColors[overallLevel];

        document.getElementById("risk-score").textContent = overallScore;
        document.getElementById("risk-level").textContent = overallLevel;
        document.getElementById("risk-level").style.color = color;
        document.getElementById("score-circle").style.borderColor = color;

        document.getElementById("result-description").textContent =
            `Assessment #${saveData.assessment_id} saved. ` +
            "Your estimate is based on 40 privacy questions.";

        renderCategoryCards(categories);
        renderRecommendations(
            categoryData.recommendations,
            overallLevel
        );

        document.getElementById("results").classList.remove("hidden");
        message.textContent = "Assessment completed successfully.";

        document.getElementById("results").scrollIntoView({
            behavior: "smooth"
        });
    } catch (error) {
        message.textContent =
            `Could not complete assessment: ${error.message}. ` +
            `Make sure Flask is running at ${API_BASE}.`;
    } finally {
        submitButton.disabled = false;
    }
});

document.getElementById("retry-button").addEventListener("click", () => {
    form.reset();
    updateCount();
    document.getElementById("results").classList.add("hidden");
    message.textContent = "";
    window.scrollTo({ top: 0, behavior: "smooth" });
});

updateCount();