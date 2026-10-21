---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.46
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.21
    win_rate: 0.71
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.6
    - name: Leviathan's Hide
      pick_rate: 0.12
      win_rate: 0.75
  - name: Sanguine Lash
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.15
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.8
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.0
  - name: Hussar's Wings
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.29
      win_rate: 0.56
    - name: Stygian Anchor
      pick_rate: 0.06
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 1.0
  - name: Adroit Ring
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Killing Stone
      pick_rate: 0.13
      win_rate: 1.0
    - name: Contagion
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.7
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.57
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-10-21'
  god_win_rate: 0.6176470588235294
  god_matches_won: 21
  god_matches_played: 34
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Leviathan''s Hide, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s
    Lament, Stone of Binding, Gluttonous Grimoire, Avenging Blade, Helm of Radiance,
    Magi''s Cloak, Shifter''s Shield, Midgardian Mail, Mantle Of Discord, Screeching
    Gargoyle, Hide of the Nemean Lion, Heartseeker, Spear of Desolation, Void Shield,
    Stampede, Daybreak Gavel, Ancile, Rod of Asclepius, Oni Hunter''s Garb, Prophetic
    Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus, Arondight, Xibalban
    Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.31
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.33
      fit: 0.5
    Gladiator's Shield:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.58
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gladiator's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Runeforged Hammer, Shield Splitter, Soul Gem,
    Eye of the Storm, Leviathan''s Hide, Berserker''s Shield, Erosion, Ethereal Staff,
    Eye of Providence, The Reaper, Draconic Scale, Yogi''s Necklace, Phoenix Feather,
    Hydra''s Lament, Gluttonous Grimoire, Avenging Blade, Chandra''s Grace, Glorious
    Pridwen, Lifebinder, Stone of Binding, Midgardian Mail, Shifter''s Shield, Helm
    of Radiance, Daybreak Gavel, Hide of the Nemean Lion, Magi''s Cloak, Sphere of
    Negation, Void Shield, Stampede, Ancile, Screeching Gargoyle, Oni Hunter''s Garb,
    Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.28
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.28
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.33
      fit: 0.46
    Gladiator's Shield:
      total: 0.69
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.6
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Heartseeker, Spear of the Magus, Void Shield, Soul Gem, Void Stone,
    Obsidian Shard, Shield Splitter, Runeforged Hammer, Titan''s Bane, The Crusher,
    Berserker''s Shield, Eye of the Storm, The Reaper, Hydra''s Lament, Erosion, Eye
    of Providence, Shield of the Phoenix, Doom Orb, Draconic Scale, Helm of Radiance,
    The World Stone, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Magi''s Cloak,
    Daybreak Gavel, Midgardian Mail, Mantle Of Discord, Rod of Asclepius, Shifter''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.22
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.33
      fit: 0.36
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Gladiator's Shield
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Runeforged
    Hammer, Soul Gem, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch
    Bow, Shogun''s Ofuda, Toxic Blade, Hydra''s Lament, Erosion, Helm of Radiance,
    Eye of the Storm, Shield of the Phoenix, Eye of Providence, Stone of Binding,
    Draconic Scale, Daybreak Gavel, Magi''s Cloak, The Reaper, Bragi''s Harp, Tekko-Kagi,
    Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Rod of Asclepius,
    Avenging Blade, Midgardian Mail, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.19
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.19
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.4
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Spear of Desolation, Hydra''s
    Lament, Soul Gem, Screeching Gargoyle, Chronos'' Pendant, Berserker''s Shield,
    Shield Splitter, Prophetic Cloak, Runeforged Hammer, Gluttonous Grimoire, Helm
    of Radiance, Erosion, Eye of Providence, Arondight, Gem of Focus, Draconic Scale,
    Eye of the Storm, Stone of Binding, Eye of Erebus, Rod of Asclepius, Spear of
    the Magus, Magi''s Cloak, Chandra''s Grace, Midgardian Mail, Glorious Pridwen,
    Daybreak Gavel, Obsidian Shard, Mantle Of Discord, Shifter''s Shield, Jade Scepter,
    Hide of the Nemean Lion, Wish-Granting Pearl, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.71
      pick: 0.33
      fit: 0.63
    Gladiator's Shield:
      total: 0.7
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.71
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Gladiator's Shield
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Lernaean
    Bow, Tekko-Kagi, Spear of Desolation, Tyrfing, Avenging Blade, Spear of the Magus,
    Erosion, Titan''s Bane, Eye of Providence, Shield of the Phoenix, Soul Gem, The
    Crusher, Helm of Radiance, Draconic Scale, Obsidian Shard, Stone of Binding, Pharaoh''s
    Curse, The Reaper, Nimble Ring, Silverbranch Bow, Magi''s Cloak, Shogun''s Ofuda,
    Screeching Gargoyle, Daybreak Gavel, Bragi''s Harp, Toxic Blade, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.22
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.47
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.23
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Gladiator's Shield
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Spear
    of the Magus, Shield Splitter, Runeforged Hammer, Soul Gem, Helm of Radiance,
    Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of
    Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Doom
    Orb, Jade Scepter, Draconic Scale, Death Metal, Stone of Binding, Wish-Granting
    Pearl, Avenging Blade, Chronos'' Pendant, The World Stone, Titan''s Bane, The
    Crusher, Ancient Signet, Magi''s Cloak, Triton''s Conch, Dreamer''s Idol, Helm
    of Darkness, Screeching Gargoyle, Daybreak Gavel, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.22
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.18
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.17
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Runeforged Hammer, Eye of the Storm,
    Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the
    Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire, Avenging Blade,
    Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Screeching
    Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Spear of Desolation,
    Void Shield, Stampede, Daybreak Gavel, Ancile, Rod of Asclepius, Oni Hunter''s
    Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus,
    Arondight, Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.59
      efficiency: 0.55
      win: 0.69
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.33
      fit: 0.5
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.15
      fit: 0.56
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
