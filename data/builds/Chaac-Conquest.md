---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.4
  slot_order:
  - name: Bancroft's Talon
    pick_rate: 0.33
    win_rate: 0.4
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.75
  - name: Breastplate of Valor
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.22
      win_rate: 0.4
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.29
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.2
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.29
    - name: Gem of Focus
      pick_rate: 0.09
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.33
  - name: Captain's Ring
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.0
    - name: Sundering Echo
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.59
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.18
  - name: Pendulum of the Ages
    pick_rate: 0.07
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-11-06'
  god_win_rate: 0.45652173913043476
  god_matches_won: 21
  god_matches_played: 46
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Shield
    Splitter, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Blood-Bound Book, Helm of Radiance, Obsidian Shard, Hydra''s
    Lament, Helm of Darkness, Death Metal, Erosion, Eye of Providence, Spear of the
    Magus, The Crusher, Shifter''s Shield, Ancient Signet, Midgardian Mail, Screeching
    Gargoyle, Heartseeker, Stone of Binding, Polynomicon, Dreamer''s Idol, Chronos''
    Pendant, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Jade Scepter.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.23
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.23
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.36
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.28
    Amanita Charm:
      total: 0.48
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Genji's Guard
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of Desolation, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Kinetic Cuirass, Shield Splitter, Berserker''s Shield, Hydra''s Lament,
    The Reaper, Ancient Signet, Oni Hunter''s Garb, Blood-Bound Book, Death Metal,
    Helm of Radiance, Runeforged Hammer, Shield of the Phoenix, Polynomicon, Obsidian
    Shard, Heartseeker, Helm of Darkness, Spear of the Magus, Draconic Scale, Chronos''
    Pendant, The Crusher, Screeching Gargoyle, Erosion, Dreamer''s Idol, Doom Orb,
    Eye of Providence, Jade Scepter, Midgardian Mail, Shifter''s Shield, Heartwood
    Charm, Stone of Binding.'
  slot_scores:
    Book of Thoth:
      total: 0.38
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.23
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.27
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.27
    Transcendence:
      total: 0.39
      efficiency: 0.5
      win: 0.4
      pick: 0.0
      fit: 0.23
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.36
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Genji's Guard
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of Desolation, Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield, Shield Splitter,
    The Reaper, Shield of the Phoenix, Obsidian Shard, Hydra''s Lament, Spear of the
    Magus, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance, Runeforged Hammer,
    The Crusher, Draconic Scale, Screeching Gargoyle, Heartseeker, Dreamer''s Idol,
    Death Metal, Chronos'' Pendant, Helm of Darkness, Ancient Signet, Erosion, Eye
    of Providence, Titan''s Bane, Polynomicon, Midgardian Mail, Shifter''s Shield,
    Doom Orb, Stone of Binding, Leviathan''s Hide, Arondight, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.13
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.26
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.26
    Transcendence:
      total: 0.37
      efficiency: 0.5
      win: 0.4
      pick: 0.0
      fit: 0.13
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.45
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Amanita Charm, Soul Gem, Rod of Tahuti, The Reaper,
    Shield of the Phoenix, Gluttonous Grimoire, Blood-Bound Book, Kinetic Cuirass,
    Jotunn''s Revenge, Berserker''s Shield, Ethereal Staff, Phoenix Feather, Yogi''s
    Necklace, Shield Splitter, Runeforged Hammer, Chandra''s Grace, Oni Hunter''s
    Garb, Draconic Scale, Obsidian Shard, Hydra''s Lament, Helm of Radiance, Death
    Metal, Sphere of Negation, Bloodforge, Erosion, The Crusher, Spear of the Magus,
    Regrowth Striders, Ancient Signet, Eye of Providence, Helm of Darkness, Midgardian
    Mail, Heartseeker, Shifter''s Shield, Jade Scepter, Lifebinder.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.2
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.37
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.2
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.51
      efficiency: 0.58
      win: 0.4
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Genji's Guard
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of Desolation, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s
    Revenge, Soul Gem, Amanita Charm, Kinetic Cuirass, Screeching Gargoyle, Stone
    of Binding, The Reaper, Berserker''s Shield, Shield Splitter, Avenging Blade,
    Void Stone, Obsidian Shard, Void Shield, Spear of the Magus, The Crusher, Heartseeker,
    Dreamer''s Idol, Shield of the Phoenix, Runeforged Hammer, Blood-Bound Book, Oni
    Hunter''s Garb, Titan''s Bane, Helm of Radiance, Draconic Scale, Hydra''s Lament,
    Death Metal, Doom Orb, Ancient Signet, Helm of Darkness, Erosion, Eye of Providence,
    The World Stone, Midgardian Mail, Shifter''s Shield, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.48
      win: 0.4
      pick: 0.0
      fit: 0.12
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.19
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.19
    Transcendence:
      total: 0.37
      efficiency: 0.5
      win: 0.4
      pick: 0.0
      fit: 0.13
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.44
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Genji's Guard
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  flex_slots:
  - Tyrfing
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Spear of Desolation, Rod of Tahuti, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Tyrfing, Shield
    Splitter, Nimble Ring, Golden Blade, Shield of the Phoenix, Blood-Bound Book,
    Oni Hunter''s Garb, The Reaper, Helm of Radiance, Bragi''s Harp, Obsidian Shard,
    Runeforged Hammer, Draconic Scale, Toxic Blade, Ancient Signet, Hydra''s Lament,
    Silverbranch Bow, Spear of the Magus, Death Metal, Helm of Darkness, Erosion,
    Polynomicon, Shogun''s Ofuda, Screeching Gargoyle, Pharaoh''s Curse, Tekko-Kagi,
    Eye of Providence, Bracer of The Abyss, Midgardian Mail, The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.72
      win: 0.4
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.17
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.17
    Tyrfing:
      total: 0.44
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.47
    Nimble Ring:
      total: 0.43
      efficiency: 0.57
      win: 0.4
      pick: 0.0
      fit: 0.33
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.27
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Rod of Tahuti,
    Soul Gem, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament,
    Shield Splitter, Chronos'' Pendant, Oni Hunter''s Garb, Draconic Scale, Gladiator''s
    Shield, The Reaper, Arondight, Blood-Bound Book, Erosion, Helm of Radiance, Runeforged
    Hammer, Eye of Providence, Obsidian Shard, Shifter''s Shield, Midgardian Mail,
    Heartwood Charm, Helm of Darkness, Stone of Binding, Ancient Signet, Chandra''s
    Grace, Spear of the Magus, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord,
    Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.3
      fit: 0.4
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.47
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.4
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.75
      pick: 0.09
      fit: 0.47
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.82
      win: 0.4
      pick: 0.0
      fit: 0.21
    Soul Gem:
      total: 0.48
      efficiency: 0.58
      win: 0.4
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Shield Splitter, Spear
    of Desolation, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Blood-Bound Book, Helm of Radiance, Obsidian Shard, Hydra''s
    Lament, Helm of Darkness, Death Metal, Erosion, Eye of Providence, Spear of the
    Magus, The Crusher, Shifter''s Shield, Ancient Signet, Midgardian Mail, Screeching
    Gargoyle, Heartseeker, Stone of Binding, Polynomicon, Dreamer''s Idol, Chronos''
    Pendant, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Jade Scepter.'
  slot_scores:
    Berserker's Shield:
      total: 0.45
      efficiency: 0.66
      win: 0.4
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.31
      fit: 0.23
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.45
      efficiency: 0.58
      win: 0.4
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  starter: *id001
---
