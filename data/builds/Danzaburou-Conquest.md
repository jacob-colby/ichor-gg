---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.6
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.35
    win_rate: 0.63
    alternates:
    - name: Transcendence
      pick_rate: 0.28
      win_rate: 0.46
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.35
  - name: Dagger of Frenzy
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.38
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.59
  - name: The Executioner
    pick_rate: 0.11
    win_rate: 0.61
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.68
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.43
  - name: Rod of Tahuti
    pick_rate: 0.09
    win_rate: 0.62
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.66
    - name: Dominance
      pick_rate: 0.08
      win_rate: 0.66
  - name: Silverbranch Bow
    pick_rate: 0.1
    win_rate: 0.74
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.39
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.7
  - name: Obsidian Shard
    pick_rate: 0.07
    win_rate: 0.47
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.47
    - name: Manchu Bow
      pick_rate: 0.05
      win_rate: 0.58
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.65
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.53
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-10-30'
  god_win_rate: 0.53315649867374
  god_matches_won: 201
  god_matches_played: 377
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Book of Thoth
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Heartseeker, Death Metal, Nimble Ring, Dominance, Soul Gem, Riptalon,
    Lernaean Bow, Tekko-Kagi, Tyrfing, Gluttonous Grimoire, The Reaper, Spear of the
    Magus, Bragi''s Harp, Deathbringer, Hydra''s Lament, Spear of Desolation, Golden
    Blade, Demon Blade, Titan''s Bane, The Crusher, Bracer of The Abyss, Musashi''s
    Dual Swords, Toxic Blade, Doom Orb, Lotus Sickle, The World Stone, Damaru, Rage,
    Blood-Bound Book, Dreamer''s Idol, Runeforged Hammer, Arondight, Avatar''s Parashu,
    Qin''s Blade, Chronos'' Pendant, Ancient Signet, Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.59
      pick: 0.15
      fit: 0.05
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.45
    Heartseeker:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.53
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Book of Thoth
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Death Metal
  - Dominance
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Dominance
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Heartseeker, Nimble Ring, Soul Gem, Gluttonous Grimoire, Dominance, Spear
    of Desolation, Spear of the Magus, Hydra''s Lament, Lotus Sickle, Bragi''s Harp,
    Lernaean Bow, The Reaper, Tyrfing, Tekko-Kagi, Doom Orb, The World Stone, Riptalon,
    Bracer of The Abyss, Ancient Signet, Chronos'' Pendant, Deathbringer, Bancroft''s
    Talon, Blood-Bound Book, Titan''s Bane, The Crusher, Dreamer''s Idol, Golden Blade,
    Gem of Focus, Arondight, Musashi''s Dual Swords, Demon Blade, Soul Reaver, Runeforged
    Hammer, Rod of Asclepius, Polynomicon.'
  slot_scores:
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.51
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.66
      pick: 0.13
      fit: 0.5
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.31
    Heartseeker:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.55
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.35
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Dominance
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Demon Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Nimble Ring, Heartseeker, Soul Gem, Dominance, Riptalon,
    Gluttonous Grimoire, Lernaean Bow, The Reaper, Tekko-Kagi, Tyrfing, Spear of the
    Magus, Deathbringer, Spear of Desolation, Bragi''s Harp, Hydra''s Lament, Demon
    Blade, Golden Blade, Musashi''s Dual Swords, Titan''s Bane, Bracer of The Abyss,
    The Crusher, Toxic Blade, Doom Orb, Lotus Sickle, Damaru, Rage, The World Stone,
    Blood-Bound Book, Dreamer''s Idol, Chronos'' Pendant, Ancient Signet, Qin''s Blade,
    Avatar''s Parashu, Runeforged Hammer, Arondight, Bancroft''s Talon.'
  slot_scores:
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.44
    Demon Blade:
      total: 0.51
      efficiency: 0.38
      win: 0.61
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.52
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.5
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Spear of Desolation
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Heartseeker, Nimble Ring, Death Metal, Spear of Desolation, Gluttonous
    Grimoire, Spear of the Magus, The Reaper, Riptalon, Dominance, Tekko-Kagi, Hydra''s
    Lament, Lotus Sickle, Lernaean Bow, Bragi''s Harp, Tyrfing, Doom Orb, Chronos''
    Pendant, The World Stone, Titan''s Bane, Bracer of The Abyss, The Crusher, Dreamer''s
    Idol, Deathbringer, Blood-Bound Book, Ancient Signet, Pendulum Blade, Golden Blade,
    Gem of Focus, Toxic Blade, Arondight, Bancroft''s Talon, Musashi''s Dual Swords,
    The Cosmic Horror, Avatar''s Parashu, Demon Blade, Runeforged Hammer.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.41
    Heartseeker:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.53
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.33
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Heartseeker
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, The Reaper, Riptalon,
    Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius, Nimble Ring, Kinetic
    Cuirass, Death Metal, Golden Blade, Genji''s Guard, Runeforged Hammer, Blood-Bound
    Book, Ethereal Staff, Yogi''s Necklace, Freya''s Tears, Breastplate of Valor,
    Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Pharaoh''s Curse, Lernaean
    Bow, Eye of the Storm, Spear of the Magus, Tyrfing, Phoenix Feather, Shogun''s
    Ofuda, Lifebinder, Erosion, Helm of Radiance, Tekko-Kagi, Hydra''s Lament, Eye
    of Providence, Toxic Blade, Daybreak Gavel, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.3
    Heartseeker:
      total: 0.54
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.14
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Heartseeker, Soul Gem, Gluttonous Grimoire, Nimble Ring, Death Metal,
    Riptalon, The Reaper, Tekko-Kagi, Spear of the Magus, Spear of Desolation, Dominance,
    Titan''s Bane, The Crusher, Lernaean Bow, Tyrfing, Doom Orb, Avenging Blade, Toxic
    Blade, The World Stone, Hydra''s Lament, Dreamer''s Idol, Bragi''s Harp, Deathbringer,
    Avatar''s Parashu, Golden Blade, Bracer of The Abyss, Pendulum Blade, Demon Blade,
    Musashi''s Dual Swords, Lotus Sickle, The Cosmic Horror, Oath-Sworn Spear, Blood-Bound
    Book, Ancient Signet, Chronos'' Pendant, Runeforged Hammer.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.55
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.58
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.65
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.35
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Riptalon
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Heartseeker, Death Metal, Riptalon, Tyrfing, Dominance,
    Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Spear of the Magus, Spear of Desolation, Bragi''s Harp, Toxic Blade, Hydra''s
    Lament, Deathbringer, Bracer of The Abyss, Qin''s Blade, Demon Blade, Titan''s
    Bane, The Crusher, Lotus Sickle, Musashi''s Dual Swords, Doom Orb, The World Stone,
    Blood-Bound Book, Dreamer''s Idol, Ancient Signet, Chronos'' Pendant, Sun Beam
    Bow, Runeforged Hammer, Arondight, Damaru, Bancroft''s Talon, Rage.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.52
    Heartseeker:
      total: 0.55
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.17
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Hydra's Lament
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Spear of Desolation,
    Death Metal, Heartseeker, Hydra''s Lament, Lotus Sickle, Gluttonous Grimoire,
    Chronos'' Pendant, Dominance, Spear of the Magus, Riptalon, Lernaean Bow, The
    Reaper, Tyrfing, Gem of Focus, Arondight, Tekko-Kagi, Bragi''s Harp, Bracer of
    The Abyss, Pendulum Blade, Deathbringer, Doom Orb, Blood-Bound Book, The World
    Stone, Golden Blade, Titan''s Bane, Ancient Signet, Totem of Death, The Crusher,
    Dreamer''s Idol, Toxic Blade, Genji''s Guard, Breastplate of Valor, Bancroft''s
    Talon, Musashi''s Dual Swords, Demon Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.47
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.34
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.2
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Heartseeker,
    Gluttonous Grimoire, Spear of Desolation, Spear of the Magus, Dominance, Lotus
    Sickle, Bragi''s Harp, Hydra''s Lament, The Reaper, Lernaean Bow, Riptalon, Bracer
    of The Abyss, Chronos'' Pendant, Tekko-Kagi, Tyrfing, Doom Orb, The World Stone,
    Dreamer''s Idol, Blood-Bound Book, Ancient Signet, Deathbringer, Gem of Focus,
    Titan''s Bane, Bancroft''s Talon, The Crusher, Golden Blade, Arondight, Rod of
    Asclepius, The Cosmic Horror, Musashi''s Dual Swords, Toxic Blade, Demon Blade,
    Typhon’s Heart, Polynomicon.'
  slot_scores:
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.45
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.35
    Heartseeker:
      total: 0.55
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.47
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.34
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Heartseeker
  - Book of Thoth
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Heartseeker,
    Soul Gem, Gluttonous Grimoire, Spear of the Magus, Dominance, Spear of Desolation,
    Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi, Riptalon, Tyrfing, Bracer
    of The Abyss, Hydra''s Lament, Doom Orb, Deathbringer, Lotus Sickle, The World
    Stone, Titan''s Bane, The Crusher, Dreamer''s Idol, Golden Blade, Blood-Bound
    Book, Ancient Signet, Chronos'' Pendant, Demon Blade, Musashi''s Dual Swords,
    Bancroft''s Talon, Toxic Blade, The Cosmic Horror, Runeforged Hammer, Gem of Focus,
    Avatar''s Parashu, Arondight, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.59
      pick: 0.15
      fit: 0.18
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.39
    Heartseeker:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.13
      fit: 0.53
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Death Metal, Nimble Ring, Soul Gem, Riptalon, Lernaean
    Bow, Tekko-Kagi, Tyrfing, Gluttonous Grimoire, The Reaper, Spear of the Magus,
    Bragi''s Harp, Deathbringer, Heartseeker, Hydra''s Lament, Dominance, Spear of
    Desolation, Golden Blade, Demon Blade, Titan''s Bane, The Crusher, Bracer of The
    Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Lotus Sickle, The World
    Stone, Damaru, Rage, Blood-Bound Book, Dreamer''s Idol, Runeforged Hammer, Arondight,
    Avatar''s Parashu, Qin''s Blade, Chronos'' Pendant, Ancient Signet, Pendulum Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.69
      win: 0.38
      pick: 0.18
      fit: 0.37
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.2
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Nimble Ring
  - Death Metal
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Devourer's Gauntlet
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Soul Gem,
    Riptalon, Lernaean Bow, Tekko-Kagi, Tyrfing, Gluttonous Grimoire, The Reaper,
    Spear of the Magus, Bragi''s Harp, Deathbringer, Heartseeker, Hydra''s Lament,
    Dominance, Spear of Desolation, Golden Blade, Demon Blade, Titan''s Bane, The
    Crusher, Bracer of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Lotus
    Sickle, The World Stone, Damaru, Rage, Blood-Bound Book, Dreamer''s Idol, Runeforged
    Hammer, Arondight, Avatar''s Parashu, Qin''s Blade, Chronos'' Pendant, Ancient
    Signet, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.69
      win: 0.38
      pick: 0.18
      fit: 0.37
    Devourer's Gauntlet:
      total: 0.46
      efficiency: 0.32
      win: 0.63
      pick: 0.35
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.74
      pick: 0.22
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.62
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Silverbranch Bow
  - Rod of Tahuti
  swaps:
  - added: Silverbranch Bow
    removed: Lernaean Bow
    reason: community 74% win over 38 matches (vs 53% on this god), taking the model's
      weakest slot from Lernaean Bow
  - added: Devourer's Gauntlet
    removed: Soul Gem
    reason: community 63% win over 132 matches (vs 53% on this god), taking the model's
      weakest slot from Soul Gem
  starter: *id001
---
