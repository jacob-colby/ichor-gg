---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.36
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.44
    win_rate: 0.42
    alternates:
    - name: Scepter of Dominion
      pick_rate: 0.1
      win_rate: 0.1
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.43
  - name: Prophetic Cloak
    pick_rate: 0.12
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.67
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.41
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.44
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.33
  - name: Spirit Robe
    pick_rate: 0.11
    win_rate: 0.18
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.6
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.2
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.11
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.43
  - name: Survivor's Sash
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.25
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.43
  - name: Heroism
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-28'
  god_win_rate: 0.39805825242718446
  god_matches_won: 41
  god_matches_played: 103
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Runeforged Hammer
  - Shifter's Shield
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous
    Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Rod of Tahuti,
    Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic Scale, Shogun''s
    Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of
    Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian Mail, Triton''s
    Conch, Stone of Binding, Dominance, Hide of the Nemean Lion, Spear of the Magus,
    Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The Crusher, Void
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.17
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.37
    Gladiator's Shield:
      total: 0.5
      efficiency: 0.39
      win: 0.63
      pick: 0.11
      fit: 0.47
    Runeforged Hammer:
      total: 0.48
      efficiency: 0.57
      win: 0.43
      pick: 0.07
      fit: 0.56
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.42
      pick: 0.44
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Gladiator's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Berserker''s Shield, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius, Shield Splitter, Eye
    of the Storm, Soul Gem, Erosion, Ethereal Staff, The Reaper, Breastplate of Valor,
    Eye of Providence, Yogi''s Necklace, Draconic Scale, Phoenix Feather, Gluttonous
    Grimoire, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean Bow, Rod
    of Tahuti, Hydra''s Lament, Lifebinder, Stone of Binding, Midgardian Mail, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean Lion, Magi''s
    Cloak, Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Heartseeker,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.2
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.48
    Gladiator's Shield:
      total: 0.5
      efficiency: 0.39
      win: 0.63
      pick: 0.11
      fit: 0.51
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.57
      win: 0.43
      pick: 0.07
      fit: 0.53
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.42
      pick: 0.44
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gladiator's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Runeforged Hammer, Rod of Tahuti, Gluttonous
    Grimoire, Berserker''s Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear
    of the Magus, Stone of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi,
    Titan''s Bane, Kinetic Cuirass, The Crusher, Soul Gem, Void Shield, Screeching
    Gargoyle, The Reaper, Void Stone, Breastplate of Valor, Shield Splitter, Doom
    Orb, Eye of the Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean
    Bow, Dreamer''s Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance,
    Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the
    Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.12
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.56
    Gladiator's Shield:
      total: 0.48
      efficiency: 0.39
      win: 0.63
      pick: 0.11
      fit: 0.36
    Runeforged Hammer:
      total: 0.46
      efficiency: 0.57
      win: 0.43
      pick: 0.07
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.55
      win: 0.36
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.42
      pick: 0.44
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Gladiator's Shield
  - Nimble Ring
  - Runeforged Hammer
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Runeforged Hammer, Nimble Ring, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing, Riptalon, Kinetic Cuirass,
    Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse, Breastplate of
    Valor, Soul Gem, Shogun''s Ofuda, Rod of Tahuti, Shield Splitter, Tekko-Kagi,
    Bragi''s Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak Gavel,
    Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of Asclepius,
    Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence, Qin''s
    Blade, Vital Amplifier, Heartseeker, Draconic Scale, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.36
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.46
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.11
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.45
    Gladiator's Shield:
      total: 0.48
      efficiency: 0.39
      win: 0.63
      pick: 0.11
      fit: 0.34
    Nimble Ring:
      total: 0.45
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.36
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.57
      win: 0.43
      pick: 0.07
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Jotunn''s Revenge,
    Breastplate of Valor, Berserker''s Shield, Runeforged Hammer, Amanita Charm, Spear
    of Desolation, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Chronos'' Pendant,
    Kinetic Cuirass, Screeching Gargoyle, Rod of Tahuti, Gluttonous Grimoire, Arondight,
    Gem of Focus, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of Asclepius,
    Shield Splitter, Spear of the Magus, Chandra''s Grace, Eye of the Storm, Daybreak
    Gavel, Obsidian Shard, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean Bow,
    Eye of Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Draconic
    Scale, Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.44
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.49
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.39
      win: 0.63
      pick: 0.11
      fit: 0.67
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.41
      pick: 0.26
      fit: 0.52
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.42
      pick: 0.44
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor,
    Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Triton''s Conch, Stone of Binding, Dominance, Hide of the Nemean Lion, Spear
    of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The
    Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.36
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.36
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.36
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.43
      efficiency: 0.55
      win: 0.36
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.48
      efficiency: 0.57
      win: 0.43
      pick: 0.07
      fit: 0.56
    Amanita Charm:
      total: 0.46
      efficiency: 0.65
      win: 0.36
      pick: 0.0
      fit: 0.45
  starter: *id001
---
