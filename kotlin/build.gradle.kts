// إعداد مشروع Gradle - Gradle project config - Gradle پروجیکٹ کنفیگریشن
plugins {
    kotlin("jvm") version "1.9.22"
    application
}

group = "com.4jawaly"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("org.json:json:20240303")
}

kotlin {
    jvmToolchain(11)
}

application {
    mainClass.set("SendTextKt")
}
