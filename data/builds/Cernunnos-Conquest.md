---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.48
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.39
    win_rate: 0.64
    alternates:
    - name: Tyrfing
      pick_rate: 0.32
      win_rate: 0.48
    - name: Avenging Blade
      pick_rate: 0.06
      win_rate: 0.75
  - name: Dagger of Frenzy
    pick_rate: 0.31
    win_rate: 0.59
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.55
    - name: Toxic Blade
      pick_rate: 0.1
      win_rate: 0.29
  - name: Odysseus' Bow
    pick_rate: 0.24
    win_rate: 0.59
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.13
      win_rate: 0.67
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.56
  - name: Riptalon
    pick_rate: 0.21
    win_rate: 0.67
    alternates:
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.6
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.11
    win_rate: 1.0
    alternates:
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.71
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.5
  - name: Manchu Bow
    pick_rate: 0.14
    win_rate: 0.43
    alternates:
    - name: Bow
      pick_rate: 0.08
      win_rate: 0.5
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.46
    win_rate: 0.73
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.15
  - name: Death's Embrace
    pick_rate: 0.08
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-08-13'
  god_win_rate: 0.5694444444444444
  god_matches_won: 41
  god_matches_played: 72
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Death
    Metal, Berserker''s Shield, Genji''s Guard, Damaru, Lernaean Bow, Spear of the
    Magus, Hydra''s Lament, Bracer of The Abyss, The Cosmic Horror, Breastplate of
    Valor, Bragi''s Harp, Golden Blade, Spear of Desolation, Blood-Bound Book, The
    Reaper, Bancroft''s Talon, Nimble Ring, Obsidian Shard, Chronos'' Pendant, Tekko-Kagi,
    Pharaoh''s Curse, Runeforged Hammer, Dominance, Helm of Radiance, Kinetic Cuirass,
    Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Jade Scepter,
    Heartseeker, Eye of Providence, The World Stone, Doom Orb.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.42
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.34
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.4
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Death Metal, The Crusher,
    Berserker''s Shield, Genji''s Guard, Damaru, Spear of the Magus, Lernaean Bow,
    The Cosmic Horror, Hydra''s Lament, Bracer of The Abyss, Breastplate of Valor,
    Spear of Desolation, Blood-Bound Book, Bragi''s Harp, Bancroft''s Talon, Golden
    Blade, Obsidian Shard, The Reaper, Nimble Ring, Chronos'' Pendant, Pharaoh''s
    Curse, Runeforged Hammer, Helm of Radiance, Tekko-Kagi, Dominance, Kinetic Cuirass,
    Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Jade Scepter,
    Eye of Providence, The World Stone, Doom Orb, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.41
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.33
    Damaru:
      total: 0.52
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.36
    Demon Blade:
      total: 0.48
      efficiency: 0.37
      win: 0.59
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Avenging Blade
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Genji''s Guard,
    Death Metal, Berserker''s Shield, Spear of the Magus, Hydra''s Lament, The Cosmic
    Horror, Spear of Desolation, Breastplate of Valor, Damaru, Lernaean Bow, Bracer
    of The Abyss, The Reaper, Obsidian Shard, Chronos'' Pendant, Golden Blade, Blood-Bound
    Book, Bragi''s Harp, Bancroft''s Talon, Tekko-Kagi, Runeforged Hammer, Freya''s
    Tears, Nimble Ring, Pharaoh''s Curse, Kinetic Cuirass, Helm of Radiance, Dominance,
    Amanita Charm, Heartseeker, The World Stone, Doom Orb, Oni Hunter''s Garb, Dreamer''s
    Idol, Shield of the Phoenix, Rod of Asclepius.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.23
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.59
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.43
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.37
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Avenging Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Shield
    of the Phoenix, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon, Jotunn''s
    Revenge, Genji''s Guard, The Crusher, Kinetic Cuirass, The Reaper, Death Metal,
    Chandra''s Grace, Breastplate of Valor, Pharaoh''s Curse, Oni Hunter''s Garb,
    Golden Blade, Hydra''s Lament, Spear of the Magus, Freya''s Tears, Damaru, Lernaean
    Bow, Runeforged Hammer, Lifebinder, The Cosmic Horror, Phoenix Feather, Shogun''s
    Ofuda, Bracer of The Abyss, Spectral Armor, Helm of Radiance, Umbral Link, Jade
    Scepter, Shifter''s Shield, Erosion, Yogi''s Necklace, Spear of Desolation, Shield
    Splitter.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.32
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.27
    Riptalon:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.6
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.25
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - The Crusher
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge,
    The Crusher, Spear of the Magus, Death Metal, Berserker''s Shield, The Cosmic
    Horror, Genji''s Guard, Spear of Desolation, The Reaper, Damaru, Lernaean Bow,
    Obsidian Shard, Hydra''s Lament, Screeching Gargoyle, Breastplate of Valor, Bracer
    of The Abyss, Tekko-Kagi, Golden Blade, Blood-Bound Book, Bragi''s Harp, Bancroft''s
    Talon, Heartseeker, The World Stone, Doom Orb, Stone of Binding, Dreamer''s Idol,
    Runeforged Hammer, Pharaoh''s Curse, Chronos'' Pendant, Nimble Ring, Kinetic Cuirass,
    Dominance, Void Shield, Helm of Radiance, Amanita Charm.'
  slot_scores:
    Avenging Blade:
      total: 0.59
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.53
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.5
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.44
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Avenging Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Death Metal, Genji''s Guard, Golden Blade, Lernaean Bow, Spear of the
    Magus, Bracer of The Abyss, Damaru, Hydra''s Lament, The Cosmic Horror, Breastplate
    of Valor, Bragi''s Harp, Blood-Bound Book, Spear of Desolation, Bancroft''s Talon,
    Pharaoh''s Curse, Nimble Ring, Obsidian Shard, Chronos'' Pendant, The Reaper,
    Runeforged Hammer, Kinetic Cuirass, Dominance, Helm of Radiance, Amanita Charm,
    Tekko-Kagi, Oni Hunter''s Garb, Rod of Asclepius, Freya''s Tears, Eye of Providence,
    Shogun''s Ofuda, Jade Scepter, Shield of the Phoenix, Toxic Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.52
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Genji''s
    Guard, Gluttonous Grimoire, Breastplate of Valor, Hydra''s Lament, The Crusher,
    Berserker''s Shield, Spear of Desolation, Death Metal, Chronos'' Pendant, Freya''s
    Tears, Damaru, Lernaean Bow, Spear of the Magus, Shield of the Phoenix, The Cosmic
    Horror, Bracer of The Abyss, Gem of Focus, Screeching Gargoyle, Golden Blade,
    Pharaoh''s Curse, Totem of Death, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Kinetic Cuirass, The Reaper, Obsidian Shard, Amanita Charm, Nimble Ring,
    Arondight, Bragi''s Harp, Runeforged Hammer, Oni Hunter''s Garb, Pendulum Blade,
    Eye of Providence, Dominance, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.59
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.31
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The
    Crusher, Death Metal, Berserker''s Shield, Genji''s Guard, Damaru, Lernaean Bow,
    Spear of the Magus, Hydra''s Lament, Bracer of The Abyss, The Cosmic Horror, Breastplate
    of Valor, Bragi''s Harp, Golden Blade, Spear of Desolation, Blood-Bound Book,
    The Reaper, Bancroft''s Talon, Nimble Ring, Obsidian Shard, Chronos'' Pendant,
    Tekko-Kagi, Pharaoh''s Curse, Runeforged Hammer, Dominance, Helm of Radiance,
    Kinetic Cuirass, Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb, Freya''s
    Tears, Jade Scepter, Heartseeker, Eye of Providence, The World Stone, Doom Orb.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Death
    Metal, Blood-Bound Book, Bancroft''s Talon, The Reaper, Berserker''s Shield, Amanita
    Charm, Rod of Asclepius, Genji''s Guard, Damaru, Shield of the Phoenix, Spear
    of the Magus, Hydra''s Lament, The Cosmic Horror, Breastplate of Valor, Lernaean
    Bow, Runeforged Hammer, Golden Blade, Chandra''s Grace, Kinetic Cuirass, Spear
    of Desolation, Bracer of The Abyss, Oni Hunter''s Garb, Obsidian Shard, Pharaoh''s
    Curse, Chronos'' Pendant, Jade Scepter, Bragi''s Harp, Lifebinder, Nimble Ring,
    Helm of Radiance, Yogi''s Necklace, Bloodforge, Freya''s Tears, Ethereal Staff,
    Wish-Granting Pearl.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.57
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.25
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Deathbringer
  flex_slots:
  - Damaru
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, Berserker''s Shield,
    The Crusher, Blood-Bound Book, Death Metal, Bancroft''s Talon, Amanita Charm,
    The Reaper, Rod of Asclepius, Genji''s Guard, Shield of the Phoenix, Damaru, Spear
    of the Magus, Hydra''s Lament, Lernaean Bow, The Cosmic Horror, Breastplate of
    Valor, Golden Blade, Bracer of The Abyss, Pharaoh''s Curse, Chandra''s Grace,
    Runeforged Hammer, Kinetic Cuirass, Spear of Desolation, Oni Hunter''s Garb, Nimble
    Ring, Obsidian Shard, Bragi''s Harp, Chronos'' Pendant, Jade Scepter, Lifebinder,
    Helm of Radiance, Shogun''s Ofuda, Yogi''s Necklace, Dominance, Freya''s Tears,
    Tekko-Kagi.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.29
    Death Metal:
      total: 0.53
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.6
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.29
    Damaru:
      total: 0.52
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.31
    Deathbringer:
      total: 0.47
      efficiency: 0.45
      win: 0.59
      pick: 0.0
      fit: 0.31
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, The Reaper,
    Blood-Bound Book, Genji''s Guard, Bancroft''s Talon, Berserker''s Shield, Death
    Metal, Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Spear of the Magus,
    Hydra''s Lament, The Cosmic Horror, Breastplate of Valor, Spear of Desolation,
    Damaru, Chandra''s Grace, Runeforged Hammer, Lernaean Bow, Obsidian Shard, Kinetic
    Cuirass, Chronos'' Pendant, Golden Blade, Bracer of The Abyss, Oni Hunter''s Garb,
    Pharaoh''s Curse, Freya''s Tears, Jade Scepter, Lifebinder, Helm of Radiance,
    Bragi''s Harp, Nimble Ring, Yogi''s Necklace, Heartseeker, Tekko-Kagi, The World
    Stone.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.3
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.59
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.59
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.29
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.41
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Berserker''s Shield, Blood-Bound Book, Bancroft''s Talon, Rod of Asclepius, Jotunn''s
    Revenge, The Reaper, Genji''s Guard, The Crusher, Kinetic Cuirass, Death Metal,
    Chandra''s Grace, Breastplate of Valor, Oni Hunter''s Garb, Pharaoh''s Curse,
    Hydra''s Lament, Spear of the Magus, Damaru, Freya''s Tears, Runeforged Hammer,
    Lifebinder, The Cosmic Horror, Umbral Link, Phoenix Feather, Golden Blade, Lernaean
    Bow, Spectral Armor, Helm of Radiance, Shogun''s Ofuda, Jade Scepter, Bracer of
    The Abyss, Bloodforge, Shifter''s Shield, Erosion, Yogi''s Necklace, Spear of
    Desolation, Shield Splitter.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.32
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.28
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.58
    Silverbranch Bow:
      total: 0.68
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.2
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - The Crusher
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, The Reaper, Blood-Bound Book, Spear of the Magus, Bancroft''s Talon,
    Berserker''s Shield, Death Metal, Amanita Charm, The Cosmic Horror, Genji''s Guard,
    Rod of Asclepius, Shield of the Phoenix, Spear of Desolation, Damaru, Hydra''s
    Lament, Obsidian Shard, Screeching Gargoyle, Breastplate of Valor, Runeforged
    Hammer, Lernaean Bow, Chandra''s Grace, Kinetic Cuirass, Golden Blade, Void Shield,
    Oni Hunter''s Garb, Bracer of The Abyss, Stone of Binding, Heartseeker, Tekko-Kagi,
    Pharaoh''s Curse, The World Stone, Doom Orb, Dreamer''s Idol, Chronos'' Pendant,
    Jade Scepter.'
  slot_scores:
    Avenging Blade:
      total: 0.6
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.6
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.65
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.35
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.48
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Berserker''s Shield, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Blood-Bound Book, Golden Blade, Bancroft''s Talon,
    Death Metal, Genji''s Guard, Rod of Asclepius, The Reaper, Shield of the Phoenix,
    Lernaean Bow, Spear of the Magus, Bracer of The Abyss, Damaru, Hydra''s Lament,
    Breastplate of Valor, The Cosmic Horror, Pharaoh''s Curse, Chandra''s Grace, Kinetic
    Cuirass, Runeforged Hammer, Oni Hunter''s Garb, Bragi''s Harp, Spear of Desolation,
    Obsidian Shard, Nimble Ring, Chronos'' Pendant, Jade Scepter, Shogun''s Ofuda,
    Lifebinder, Helm of Radiance, Dominance, Yogi''s Necklace, Toxic Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.27
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.28
    Riptalon:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.35
      fit: 0.69
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.42
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.66
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Avenging Blade
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s
    Revenge, Genji''s Guard, Shield of the Phoenix, Breastplate of Valor, Hydra''s
    Lament, Berserker''s Shield, The Crusher, Chandra''s Grace, Amanita Charm, Blood-Bound
    Book, Bancroft''s Talon, The Reaper, Spear of Desolation, Rod of Asclepius, Death
    Metal, Chronos'' Pendant, Freya''s Tears, Spear of the Magus, Damaru, The Cosmic
    Horror, Kinetic Cuirass, Lernaean Bow, Runeforged Hammer, Oni Hunter''s Garb,
    Gem of Focus, Golden Blade, Pharaoh''s Curse, Screeching Gargoyle, Bracer of The
    Abyss, Totem of Death, Obsidian Shard, Yogi''s Necklace, Jade Scepter, Arondight,
    Lifebinder, Eye of Providence, Spectral Armor.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.48
      win: 0.75
      pick: 0.06
      fit: 0.26
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.59
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.54
      win: 1.0
      pick: 0.24
      fit: 0.23
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, The
    Crusher, Death Metal, Blood-Bound Book, Bancroft''s Talon, The Reaper, Berserker''s
    Shield, Amanita Charm, Rod of Asclepius, Genji''s Guard, Damaru, Shield of the
    Phoenix, Spear of the Magus, Hydra''s Lament, The Cosmic Horror, Breastplate of
    Valor, Lernaean Bow, Runeforged Hammer, Golden Blade, Chandra''s Grace, Kinetic
    Cuirass, Spear of Desolation, Bracer of The Abyss, Oni Hunter''s Garb, Obsidian
    Shard, Pharaoh''s Curse, Chronos'' Pendant, Jade Scepter, Bragi''s Harp, Lifebinder,
    Nimble Ring, Helm of Radiance, Yogi''s Necklace, Bloodforge, Freya''s Tears, Ethereal
    Staff, Wish-Granting Pearl.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
---
