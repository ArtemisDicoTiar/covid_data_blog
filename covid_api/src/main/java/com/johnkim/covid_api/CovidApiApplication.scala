package com.integration

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.context.annotation.Bean
import org.springframework.web.servlet.config.annotation.{CorsRegistry, WebMvcConfigurer, WebMvcConfigurerAdapter}

@SpringBootApplication
class SpringBootIntegration {
    @Bean
    def CovidApiApplication(): WebMvcConfigurer = {
        new WebMvcConfigurerAdapter() {
            override def addCorsMappings(registry: CorsRegistry): Unit = {
                registry.addMapping("/**").allowedOrigins("*").allowedMethods("*")
            }
        }
    }
}

object CovidApiApplication extends App {
    SpringApplication.run(classOf[SpringBootIntegration])
}
